from abc import ABC, abstractmethod

from application.dto.ability_output import AbilityOutputDto


class AbilityPresenter(ABC):
    @abstractmethod
    def present(self, ability_data: AbilityOutputDto) -> dict:
        pass
