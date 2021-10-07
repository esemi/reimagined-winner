"""Partner entities."""

from dataclasses import dataclass
from typing import Set


@dataclass(frozen=True)
class Partner:
    descrizione: str
    indirizzo: str
    cap: str
    comune: str
    provincia: str
    cf: str
    email: str = ''

    @classmethod
    def required_fields(cls) -> Set[str]:
        return {
            'descrizione',
            'indirizzo',
            'cap',
            'comune',
            'provincia',
            'cf',
        }
