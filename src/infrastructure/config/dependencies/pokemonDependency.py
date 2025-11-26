from src.application.use_cases.pokemon.create_pokemon import CreatePokemon
from src.infrastructure.database.repositories.pokemon_repository import (
    PokemonRepository,
)


def get_create_pokemon_use_case(repo: PokemonRepository) -> CreatePokemon:
    """Fábrica para el use case, inyectando el repositorio."""
    return CreatePokemon(repo=repo)
