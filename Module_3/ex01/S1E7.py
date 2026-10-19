from S1E9 import Character



class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        family_name: str = "baratheon",
        eyes: str = "brown",
        hairs: str = "dark",
    ):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        return f"Baratheon {self.first_name}: {self.eyes} eyes and {self.hairs} hairs is {'alive' if self.is_alive else 'dead'}"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> bool:
        """ddd"""
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
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        return f"Lannister {self.first_name}: {self.eyes} eyes and {self.hairs} hairs is {'alive' if self.is_alive else 'dead'}"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        return cls(first_name, is_alive)
        
    def die(self) -> bool:
        """ddd"""
        self.is_alive = False
        return self.is_alive


Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
