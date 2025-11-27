from application.dto.specie_output import SpecieOutputDto
from application.interfaces.presenters.specie_presenter import SpeciePresenter


class JsonSpeciePresenter(SpeciePresenter):

    @staticmethod
    def present(specie_data: SpecieOutputDto) -> dict:
        return {
            "uid": specie_data.uid,
            "name": specie_data.name,
            "appCreationDate": specie_data.app_creation_date.isoformat(),
            "url": specie_data.url,
        }
