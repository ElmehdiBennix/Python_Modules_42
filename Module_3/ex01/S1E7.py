"""Define the Baratheon and Lannister character families."""

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        family_name: str = "Baratheon",
        eyes: str = "brown",
        hairs: str = "dark",
    ):
        """
        Initialize a new Baratheon family member.

        Args:
            first_name (str): The character's given name.
            is_alive (bool): The character's life status,
                optional (default: True).
            family_name (str): The family house name,
                optional (default: "Baratheon").
            eyes (str): The color of the character's eyes,
                optional (default: "brown").
            hairs (str): The color/type of the character's hair,
                optional (default: "dark").
        Raises:
            TypeError: if type doesn't match class attribute.
        """
        if not isinstance(family_name, str):
            raise TypeError("family_name must be a str type")
        if not isinstance(eyes, str):
            raise TypeError("eyes must be a str type")
        if not isinstance(hairs, str):
            raise TypeError("hairs must be a str type")

        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """
        Return a human-readable Baratheon character string.
        """
        state = "alive" if self.is_alive else "dead"
        return (
            f"Baratheon {self.first_name}: {self.eyes} eyes and "
            f"{self.hairs} hairs is {state}"
        )

    def __repr__(self) -> str:
        """
        Return the vector representation of the Baratheon character traits.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> bool:
        """
        Mark the Baratheon character as dead.

        Returns:
            bool: The updated is_alive status (False).
        """
        self.is_alive = False
        return self.is_alive


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        family_name: str = "Lannister",
        eyes: str = "blue",
        hairs: str = "light",
    ):
        """
        Initialize a new Lannister family member.

        Args:
            first_name (str): The character's given name.
            is_alive (bool): The character's life status,
                optional (default: True).
            family_name (str): The family house name,
                optional (default: "Lannister").
            eyes (str): The color of the character's eyes,
                optional (default: "blue").
            hairs (str): The color/type of the character's hair,
                optional (default: "light").
        Raises:
            TypeError: if type doesn't match class attribute.
        """
        if not isinstance(family_name, str):
            raise TypeError("family_name must be a str type")
        if not isinstance(eyes, str):
            raise TypeError("eyes must be a str type")
        if not isinstance(hairs, str):
            raise TypeError("hairs must be a str type")

        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """
        Return a human-readable Lannister character string.
        """
        state = "alive" if self.is_alive else "dead"
        return (
            f"Lannister {self.first_name}: {self.eyes} eyes and "
            f"{self.hairs} hairs is {state}"
        )

    def __repr__(self) -> str:
        """
        Return the vector representation of the Lannister character traits.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        Alternative constructor for a Lannister with default traits.

        Args:
            first_name (str): The character's given name.
            is_alive (bool): The character's life status,
                optional (default: True).
        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)

    def die(self) -> bool:
        """
        Mark the Lannister character as dead.

        Returns:
            bool: The updated is_alive status (False).
        """
        self.is_alive = False
        return self.is_alive
