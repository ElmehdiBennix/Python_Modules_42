"""Define the King class through multiple inheritance."""

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represent a king with mutable eye and hair characteristics."""

    def __init__(self, first_name: str):
        """Initialize a King with the Baratheon defaults."""
        super().__init__(first_name)

    def get_eyes(self):
        """Return the king's eye color."""
        return self.eyes

    def get_hairs(self):
        """Return the king's hair color."""
        return self.hairs

    def set_eyes(self, eyes: str):
        """Set and return the king's eye color."""
        self.eyes = eyes
        return self.eyes

    def set_hairs(self, hairs: str):
        """Set and return the king's hair color."""
        self.hairs = hairs
        return self.hairs
