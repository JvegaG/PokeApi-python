from sqlalchemy import Column, DateTime, Integer, String

from src.infrastructure.database.database import Base


class PokemonModel(Base):
    __tablename__ = "pokemon"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    base_experience = Column(Integer)
    locationarea_encounters = Column(String)
    weight = Column(Integer)
    height = Column(Integer)
    app_created_by = Column(String)
    app_creation_date = Column(DateTime)
    app_last_update_by = Column(String)
    app_last_update_date = Column(DateTime)
