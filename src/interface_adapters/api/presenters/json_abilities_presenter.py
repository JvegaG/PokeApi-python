from application.dto.ability_output import AbilityOutputDto
from application.interfaces.presenters.ability_presenter import AbilityPresenter
from interface_adapters.api.presenters.json_species_presenter import JsonSpeciePresenter


class JsonAbilityPresenter(AbilityPresenter):

    @staticmethod
    def present(ability_data: AbilityOutputDto) -> dict:
        return {
            "uid": ability_data.uid,
            "specie": JsonSpeciePresenter().present(ability_data.specie),
            "appCreationDate": ability_data.app_creation_date.isoformat(),
            "isHidden": ability_data.is_hidden,
            "slot": ability_data.slot,
        }
