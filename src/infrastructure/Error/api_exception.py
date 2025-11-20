from dataclasses import dataclass


@dataclass
class ApiException(Exception):
    message: str

    def __post_init__(self) -> None:
        super().__init__(self.message)
