from abc import ABC, abstractmethod


class Character(ABC):
    """Represents a generic character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a new Character instance.

        Args:
            first_name (str): The character's given name.
            is_alive (bool): The character's current life status, optional (default: True).
        Raises:
            TypeError: if type doesn't match class attribute.
        """
        if not isinstance(first_name, str):
            raise TypeError("first name must be a str type")
        if not isinstance(is_alive, bool):
            raise TypeError("is alive must be a bool type")

        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> bool:
        """
        abstract method that handles death logic.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("test")


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a new Stark family member.

        Args:
            first_name (str): The Stark's given name.
            is_alive (bool): The Stark's current life status, optional (default: True).
        Raises:
            TypeError: if type doesn't match class attribute.
        """
        super().__init__(first_name, is_alive)

    def die(self) -> bool:
        """
        Mark the Stark character as dead.

        Returns:
            bool: The updated is_alive status (False).
        """
        self.is_alive = False
        return self.is_alive
