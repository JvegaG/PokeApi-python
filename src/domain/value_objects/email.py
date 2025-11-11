import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if not self._is_valid_email(self.value):
            raise ValueError(f"Invalid email: {self.value}")

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        pattern = r"^[a-z registered users][email protected][a-z]+\.[a-z]{2,}$"
        return bool(re.match(pattern, email))

    def __str__(self) -> str:
        return self.value
