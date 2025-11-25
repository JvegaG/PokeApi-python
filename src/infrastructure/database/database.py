import logging
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import QueuePool

from infrastructure.app import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_database_url() -> str:
    return (
        f"postgresql://{config.postgres_user}:{config.postgres_password}@"
        f"{config.postgres_host}:{config.postgres_port}/{config.postgres_db}"
    )


# Database URL Configuration
DATABASE_URL = get_database_url()

# Pool Configuration from environment or defaults
POOL_SIZE = 10
MAX_OVERFLOW = 20
POOL_TIMEOUT = 30
POOL_RECYCLE = 3600

# SQLAlchemy Engine Configuration
engine = create_engine(
    DATABASE_URL,
    # Connection Pool Settings
    poolclass=QueuePool,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
    pool_timeout=POOL_TIMEOUT,
    pool_recycle=POOL_RECYCLE,
    pool_pre_ping=True,  # Verify connections before using
    # Performance Settings
    echo=False,
    echo_pool=False,
    future=True,  # Use SQLAlchemy 2.0 style
    # Connection Arguments for PostgreSQL
    connect_args={
        "connect_timeout": 10,
        "options": "-c timezone=utc",
        "application_name": config.project_name,
    },
)

# Session Factory Configuration
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
)

# Base class for declarative models
Base = declarative_base()


# Event Listeners for PostgreSQL optimization
@event.listens_for(Engine, "connect")
def set_postgresql_pragma(dbapi_connection, connection_record):
    """
    Set PostgreSQL-specific connection parameters when connection is established.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("SET timezone='UTC'")
    cursor.execute("SET statement_timeout = '30s'")
    cursor.close()
    logger.debug("PostgreSQL connection configured")


@event.listens_for(Engine, "checkout")
def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    """Verify connection health on checkout from pool."""
    logger.debug("Connection checked out from pool")


@event.listens_for(Engine, "checkin")
def receive_checkin(dbapi_connection, connection_record):
    """Clean up on connection return to pool."""
    logger.debug("Connection returned to pool")


# Dependency Injection for FastAPI
def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a database session.
    This is the primary method to use in your API routes.

    Usage in route:
        @router.get("/pokemon")
        def get_pokemon(db: Session = Depends(get_db)):
            repo = PokemonRepository(db)
            return repo.get_all()

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


# Context Manager for manual session management
@contextmanager
def get_db_context() -> Generator[Session, None, None]:
    """
    Context manager for database sessions in non-FastAPI contexts.
    Useful for scripts, background tasks, or CLI commands.

    Usage:
        with get_db_context() as db:
            repo = PokemonRepository(db)
            pokemon = repo.get_by_id(1)

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        logger.error(f"Database context error: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


# Database Utility Functions
def init_db() -> None:
    """
    Initialize database by creating all tables.

    ⚠️ WARNING: This should ONLY be used for:
    - Initial development setup
    - Running tests with in-memory databases
    - Quick prototyping

    For production and proper development, use Alembic migrations instead:
        alembic revision --autogenerate -m "Initial migration"
        alembic upgrade head

    Usage:
        from database import init_db
        init_db()  # Only for testing/development!
    """
    try:
        # Import all models to ensure they're registered with Base
        import_all_models()

        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully (Development mode)")
        logger.warning("⚠️ Use Alembic migrations for production!")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise


def import_all_models() -> None:
    """
    Import all model modules to ensure they're registered with Base.
    This is needed for Alembic to detect model changes.

    Add imports for all your model files here.
    """
    try:
        # Import your models here so SQLAlchemy knows about them
        # Example:
        # from domain.models.pokemon_model import Pokemon, Type, PokemonAbility
        # from domain.models.user_model import User
        pass
    except ImportError as e:
        logger.warning(f"Could not import models: {str(e)}")


def drop_db() -> None:
    """
    Drop all database tables.
    WARNING: This will delete all data! Use only in development/testing.
    """
    try:
        Base.metadata.drop_all(bind=engine)
        logger.warning("All database tables dropped")
    except Exception as e:
        logger.error(f"Error dropping database tables: {str(e)}")
        raise


def check_db_connection() -> bool:
    """
    Check if database connection is healthy.

    Returns:
        bool: True if connection is successful, False otherwise
    """
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        logger.info("Database connection is healthy")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return False


def get_db_info() -> dict:
    """
    Get database connection information.
    Useful for monitoring and debugging.

    Returns:
        dict: Dictionary containing database connection details
    """
    return {
        "driver": engine.driver,
        "url": str(engine.url).replace(
            str(engine.url.password) if engine.url.password else "", "***"
        ),
        "pool_size": engine.pool.size(),
        "checked_out_connections": engine.pool.checkedout(),
        "pool_overflow": engine.pool.overflow(),
        "database_name": engine.url.database,
    }


# Health Check Function for FastAPI
async def database_health_check() -> dict:
    """
    Async health check for database connection.

    Usage in FastAPI:
        @app.get("/health")
        async def health():
            return await database_health_check()

    Returns:
        dict: Health status information
    """
    try:
        is_healthy = check_db_connection()
        return {
            "database": "healthy" if is_healthy else "unhealthy",
            "status": "ok" if is_healthy else "error",
            "details": get_db_info() if is_healthy else None,
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"database": "unhealthy", "status": "error", "error": str(e)}


# Session Scope Decorator
def with_db_session(func):
    """
    Decorator to automatically handle database session for functions.
    Useful for standalone functions outside of FastAPI routes.

    Usage:
        @with_db_session
        def get_user_count(db: Session) -> int:
            return db.query(User).count()

        # Call without passing db
        count = get_user_count()
    """

    def wrapper(*args, **kwargs):
        with get_db_context() as db:
            return func(db=db, *args, **kwargs)

    return wrapper


# Cleanup function
def close_db_connections() -> None:
    """
    Close all database connections and dispose engine.
    Should be called on application shutdown.

    Usage in FastAPI lifespan:
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            close_db_connections()
    """
    try:
        engine.dispose()
        logger.info("Database connections closed and engine disposed")
    except Exception as e:
        logger.error(f"Error closing database connections: {str(e)}")
        raise


# Transaction Management Utilities
@contextmanager
def transaction_scope():
    """
    Provide a transactional scope around a series of operations.
    Automatically commits on success and rolls back on error.

    Usage:
        with transaction_scope() as db:
            repo = PokemonRepository(db)
            repo.create(pokemon_data)
            # Automatically commits here if no exception
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Transaction failed: {str(e)}")
        raise
    finally:
        session.close()


# Database Session Metrics
def get_pool_status() -> dict:
    """
    Get detailed connection pool status.
    Useful for monitoring and performance tuning.

    Returns:
        dict: Connection pool metrics
    """
    pool = engine.pool
    return {
        "pool_size": pool.size(),
        "checked_in": pool.checkedin(),
        "checked_out": pool.checkedout(),
        "overflow": pool.overflow(),
        "queue_size": pool._queue.qsize() if hasattr(pool._queue, "qsize") else 0,
        "total_connections": pool.size() + pool.overflow(),
    }


# Export commonly used components
__all__ = [
    # Core components
    "engine",
    "SessionLocal",
    "Base",
    "DATABASE_URL",
    # Session management
    "get_db",
    "get_db_context",
    "transaction_scope",
    # Database operations
    "init_db",
    "drop_db",
    "import_all_models",
    # Health and monitoring
    "check_db_connection",
    "get_db_info",
    "get_pool_status",
    "database_health_check",
    # Utilities
    "with_db_session",
    "close_db_connections",
]
