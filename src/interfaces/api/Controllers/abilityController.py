from fastapi import APIRouter

from infrastructure.Error.api_exception import ApiException

router = APIRouter()


@router.get("/")
async def getAbility():
    try:
        return {"ability": "You have the ability!"}
    except ApiException:
        raise
    # except Exception as exception:
    #     raise ApiErrorHandling.http_error(
    #         "Unexpected error getting all cat facts", exception
    #     )


@router.get("/{ability_id}")
async def getAbilityById(ability_id: int):
    try:
        return {"ability": f"You have the ability with id {ability_id}!"}
    except ApiException:
        raise
    # except Exception as exception:
    #     raise ApiErrorHandling.http_error(
    #         "Unexpected error getting cat fact by id", exception
    #     )
