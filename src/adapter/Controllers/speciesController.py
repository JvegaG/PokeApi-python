from fastapi import APIRouter

from adapter.api.shared.api_error_handling import ApiErrorHandling

router = APIRouter()


@router.get("/")
async def getSpecies():
    try:
        return {"species": "You have a species!"}
    except Exception as exception:
        raise ApiErrorHandling.http_error(
            "Unexpected error getting all cat facts", exception
        )


@router.get("/{species_id}")
async def getSpeciesById(species_id: int):
    try:
        return {"species": f"You have the species with id {species_id}!"}
    except Exception as exception:
        raise ApiErrorHandling.http_error(
            "Unexpected error getting cat fact by id", exception
        )
