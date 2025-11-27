from application.dto.pokemon_output import PokemonOutputDto
from application.interfaces.presenters.pokemon_presenter import PokemonPresenter


class TablePokemonPresenter(PokemonPresenter):

    @staticmethod
    def present(pokemon_data: PokemonOutputDto) -> dict:
        return {
            "ID": pokemon_data.uid,
            "Name": pokemon_data.name,
            "Location": pokemon_data.locationarea_encounters,
            "Created": pokemon_data.app_creation_date.strftime("%Y-%m-%d"),
        }
