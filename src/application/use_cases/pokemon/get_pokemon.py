from application.dto.pokemon_output import PokemonOutputDto
from application.interfaces.repositories.pokemon_repository import PokemonRepository
from application.mappers.pokemon_mapper import PokemonMapper


class GetPokemonUseCase:
    def __init__(self, pokemon_repository: PokemonRepository):
        self.pokemon_repository = pokemon_repository

    async def execute(self, uid: str) -> PokemonOutputDto:
        pokemon = await self.pokemon_repository.find_by_uid(uid)

        if not pokemon:
            raise ValueError(f"Pokemon with uid:{uid} not found")

        return PokemonMapper.entity_to_output_dto(pokemon)
