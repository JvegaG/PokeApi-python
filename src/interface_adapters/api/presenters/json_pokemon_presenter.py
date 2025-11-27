from application.dto.pokemon_output import PokemonOutputDto
from application.interfaces.presenters.pokemon_presenter import PokemonPresenter


class JsonPokemonPresenter(PokemonPresenter):

    @staticmethod
    def present(pokemon_data: PokemonOutputDto) -> dict:
        return {
            "uid": pokemon_data.uid,
            "name": pokemon_data.name,
            "appCreationDate": pokemon_data.app_creation_date.isoformat(),
            "baseExperience": pokemon_data.base_experience,
            "locationAreaEncounters": pokemon_data.locationarea_encounters,
            "weight": pokemon_data.weight,
            "height": pokemon_data.height,
        }
