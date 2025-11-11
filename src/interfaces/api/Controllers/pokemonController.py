from fastapi import APIRouter

from infrastructure.Error.api_exception import ApiException

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
