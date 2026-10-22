

from decimal import DivisionByZero


class calculator:


    def __init__(self, numbers : list[float]) -> None:
        self.numbers = numbers


    def __add__(self, object) -> None:
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number + object
        print(self.numbers)


    def __mul__(self, object) -> None:
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number * object
        print(self.numbers)

    def __sub__(self, object) -> None:
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number - object
        print(self.numbers)

    def __truediv__(self, object) -> None:

        if object == 0:
            raise DivisionByZero("Error division by zero is impossible")
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number / object
        print(self.numbers)