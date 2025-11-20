from application.dto.pokemon_input import PokemonInputDto
from application.dto.pokemon_output import PokemonOutputDto
from application.interfaces.repositories.pokemon_repository import PokemonRepository
from application.mappers.pokemon_mapper import PokemonMapper


class CreatePokemon:
    def __init__(self, pokemon_repository: PokemonRepository):
        self.pokemon_repository = pokemon_repository

    async def execute(self, input_dto: PokemonInputDto) -> PokemonOutputDto:
        try:

            existing = await self.pokemon_repository.find_by_name(input_dto.name)
            if existing:
                raise ValueError(f"Pokemon with name {input_dto.name} already exists.")

            pokemon = PokemonMapper.input_dto_to_entity(input_dto)
            await self.pokemon_repository.create(pokemon)

            return PokemonMapper.entity_to_output_dto(pokemon)

        except Exception as e:
            raise ValueError(f"Invalid Pokemon data: {e}")
