
class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = 0

        for value1, value2 in zip(V1, V2):
            result += value1 * value2

        print(result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = []

        for value1, value2 in zip(V1, V2):
            result.append(float(value1) + float(value2))

        print(result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = []

        for value1, value2 in zip(V1, V2):
            result.append(float(value1) - float(value2))

        print(result)