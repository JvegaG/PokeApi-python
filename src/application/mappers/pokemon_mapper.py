from application.dto.pokemon_input import PokemonInputDto
from application.dto.pokemon_output import PokemonOutputDto
from domain.entities.pokemon import Pokemon


class PokemonMapper:
    """Mapper entre Domain Entity y Application DTOs"""

    @staticmethod
    def input_dto_to_entity(dto: PokemonInputDto) -> Pokemon:
        """Convierte DTO de entrada a Entity"""
        return Pokemon.create(
            name=dto.name,
            base_experience=dto.base_experience or 0,
            height=dto.height or 0,
            weight=dto.weight or 0,
            locationarea_encounters=dto.locationarea_encounters or "",
        )

    @staticmethod
    def entity_to_output_dto(entity: Pokemon) -> PokemonOutputDto:
        """Convierte Entity a DTO de salida"""
        return PokemonOutputDto(
            uid=entity.uid,
            app_creation_date=entity.app_creation_date,
            name=entity.name,
            base_experience=entity.base_experience,
            locationarea_encounters=entity.locationarea_encounters,
            weight=entity.weight,
            height=entity.height,
        )

    @staticmethod
    def entities_to_output_dtos(entities: list[Pokemon]) -> list[PokemonOutputDto]:
        """Convierte lista de entities a DTOs"""
        return [PokemonMapper.entity_to_output_dto(entity) for entity in entities]
