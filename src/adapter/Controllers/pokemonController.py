from fastapi import APIRouter

from adapter.api.shared.api_error_handling import ApiErrorHandling

router = APIRouter()


@router.get("/")
async def getPokemon():
    try:
        return {"pokemon": "You have a Pokemon!"}
    except Exception as exception:
        raise ApiErrorHandling.http_error(
            "Unexpected error getting all cat facts", exception
        )


@router.get("/{pokemon_id}")
async def getPokemonById(pokemon_id: int):
    try:
        return {"pokemon": f"You have the Pokemon with id {pokemon_id}!"}
    except Exception as exception:
        raise ApiErrorHandling.http_error(
            "Unexpected error getting cat fact by id", exception
        )
