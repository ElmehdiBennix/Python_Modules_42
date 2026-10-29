"""Calculate scalar operations on a mutable numeric vector."""


class calculator:
    """Apply arithmetic operations to every vector element."""

    def __init__(self, numbers: list[float]) -> None:
        """Store the vector that arithmetic operations will mutate."""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """Add a scalar to every vector element and print the result."""
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number + object
        print(self.numbers)

    def __mul__(self, object) -> None:
        """Multiply every vector element by a scalar and print the result."""
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number * object
        print(self.numbers)

    def __sub__(self, object) -> None:
        """Subtract a scalar from every vector element and print the result."""
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number - object
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """Divide every vector element by a scalar and print the result."""
        if object == 0:
            raise ZeroDivisionError("division by zero is impossible")
        for idx, number in enumerate(self.numbers):
            self.numbers[idx] = number / object
        print(self.numbers)
