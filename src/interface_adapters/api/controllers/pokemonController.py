from application.use_cases.pokemon.get_pokemon import GetPokemonUseCase
from infrastructure.config.dependencies.pokemonDependency import (
    get_by_uid_pokemon_use_case,
    get_create_pokemon_use_case,
)
from application.use_cases.pokemon.create_pokemon import CreatePokemon
from application.dto.pokemon_input import PokemonInputDto
from fastapi import APIRouter, Depends

from infrastructure.error.api_exception import ApiException

router = APIRouter()


@router.get("/")
async def getPokemon():
    try:
        return {"pokemon": "You have a Pokemon!"}
    except ApiException:
        raise


@router.get("/{pokemon_id}")
async def getPokemonById(
    pokemon_id: str,
    use_case: GetPokemonUseCase = Depends(get_by_uid_pokemon_use_case),
):
    try:
        output = await use_case.execute(pokemon_id)
        return output
    except ApiException:
        raise


@router.post("/")
async def createPokemon(
    request: PokemonInputDto,
    use_case: CreatePokemon = Depends(get_create_pokemon_use_case),
):
    try:
        output = await use_case.execute(request)
        return output
    except ApiException:
        raise
