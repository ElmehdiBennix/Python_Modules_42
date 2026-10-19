from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    def __init__(self, first_name: str, is_alive : bool = True):
        """ test """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ez"""
        raise NotImplementedError("not impelemted")

class Stark(Character):
    """ddd"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """ddd"""
        super().__init__(first_name, is_alive)

    def die(self):
        """ddd"""
        self.is_alive = False
        return self.is_alive
