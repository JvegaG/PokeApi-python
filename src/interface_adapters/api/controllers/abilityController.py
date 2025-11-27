from fastapi import APIRouter

from infrastructure.error.api_exception import ApiException

router = APIRouter()


@router.get("/")
async def getAbility():
    try:
        return {"ability": "You have the ability!"}
    except ApiException:
        raise


@router.get("/{ability_id}")
async def getAbilityById(ability_id: int):
    try:
        return {"ability": f"You have the ability with id {ability_id}!"}
    except ApiException:
        raise
