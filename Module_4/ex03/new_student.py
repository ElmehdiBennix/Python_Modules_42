"""Build a student record with a derived login and a random identifier."""

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return fifteen random lower-case letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student whose login and id are derived, never supplied."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Derive the login from the first letter of the name and surname."""
        self.login = self.name[0].upper() + self.surname
