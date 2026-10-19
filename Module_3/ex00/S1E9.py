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
        raise NotImplementedError("test")


class Stark(Character):
    """ddd"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """ddd"""
        super().__init__(first_name, is_alive)

    def die(self):
        """ddd"""
        self.is_alive = False



Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

