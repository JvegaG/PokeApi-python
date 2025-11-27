from fastapi import Depends
from sqlalchemy.orm.session import Session

from application.interfaces.repositories.pokemon_repository import (
    IPokemonRepository,
)
from application.use_cases.pokemon.create_pokemon import CreatePokemon
from application.use_cases.pokemon.get_pokemon import GetPokemonUseCase
from infrastructure.database.database import get_db
from infrastructure.database.repositories.pokemon_repository import (
    PokemonRepository,
)


def get_pokemon_repository(db: Session = Depends(get_db)) -> IPokemonRepository:
    """Fábrica para el repositorio concreto."""
    return PokemonRepository(db)


def get_create_pokemon_use_case(
    repo: IPokemonRepository = Depends(get_pokemon_repository),
) -> CreatePokemon:
    return CreatePokemon(repo)


def get_by_uid_pokemon_use_case(
    repo: IPokemonRepository = Depends(get_pokemon_repository),
) -> GetPokemonUseCase:
    return GetPokemonUseCase(repo)
