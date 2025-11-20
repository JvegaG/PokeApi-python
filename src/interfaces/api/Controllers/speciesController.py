from fastapi import APIRouter

from infrastructure.error.api_exception import ApiException

router = APIRouter()


@router.get("/")
async def getSpecies():
    try:
        return {"species": "You have a species!"}
    except ApiException:
        raise


@router.get("/{species_id}")
async def getSpeciesById(species_id: int):
    try:
        return {"species": f"You have the species with id {species_id}!"}
    except ApiException:
        raise
