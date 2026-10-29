"""Calculate dot products and element-wise vector operations."""


class calculator:
    """Provide vector operations without instance construction."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of two vectors."""
        result = 0

        for value1, value2 in zip(V1, V2):
            result += value1 * value2

        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element-wise sum of two vectors."""
        result = []

        for value1, value2 in zip(V1, V2):
            result.append(float(value1) + float(value2))

        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element-wise difference of two vectors."""
        result = []

        for value1, value2 in zip(V1, V2):
            result.append(float(value1) - float(value2))

        print(f"Sous Vector is: {result}")
