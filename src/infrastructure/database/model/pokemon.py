from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from infrastructure.database.database import Base


class PokemonModel(Base):
    __tablename__ = "pokemon"

    uid: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    base_experience: Mapped[int] = mapped_column(Integer)
    locationarea_encounters: Mapped[str] = mapped_column(String)
    weight: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    app_created_by: Mapped[str] = mapped_column(String)
    app_creation_date: Mapped[datetime] = mapped_column(DateTime)
    app_last_update_by: Mapped[str] = mapped_column(String)
    app_last_update_date: Mapped[datetime] = mapped_column(DateTime)
