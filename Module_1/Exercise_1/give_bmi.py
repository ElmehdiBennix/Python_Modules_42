
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("dataset mismatch: lists must be the same size to calculate bmi level")

    return [weight[i] / (height[i] ** 2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [bmi[i] > limit for i in range(len(bmi))]


print(__name__)