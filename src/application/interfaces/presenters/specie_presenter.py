from abc import ABC, abstractmethod

from application.dto.specie_output import SpecieOutputDto


class SpeciePresenter(ABC):
    @abstractmethod
    def present(self, specie_data: SpecieOutputDto) -> dict:
        pass
