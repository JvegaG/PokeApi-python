from src.application.use_cases.pokemon.create_pokemon import CreatePokemon
from src.application.dto.pokemon_input import PokemonInputDto
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
async def getPokemonById(pokemon_id: int):
    try:
        return {"pokemon": f"You have the Pokemon with id {pokemon_id}!"}
    except ApiException:
        raise


@router.post("/")
async def createPokemon(
    request: PokemonInputDto,
    use_case: CreatePokemon = Depends(get_create_pokemon_use_case),
):
    output = use_case.execute(request)
    return output
