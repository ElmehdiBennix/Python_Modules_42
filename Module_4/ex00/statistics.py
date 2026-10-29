from collections.abc import Callable
from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:

    def mean(data: list):
        return sum(data) / len(data)

    def median(data: list) -> float:
        """Return the middle value of data."""
        n = len(data)
        mid = n // 2
        if n % 2:
            return data[mid]
        return (data[mid - 1] + data[mid]) / 2

    def quartile(data: list) -> list[float]:
        """Return the 25% and 75% quartiles, linearly interpolated."""
        n = len(data)
        result = []
        for p in (0.25, 0.75):
            pos = p * (n - 1)
            low = int(pos)
            high = min(low + 1, n - 1)
            gap = data[high] - data[low]
            result.append(float(data[low] + gap * (pos - low)))
        return result

    def var(data: list):
        m = mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    def std(data: list):
        return var(data) ** 0.5

    states: dict[str, Callable[[list], Any]] = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "var": var,
        "std": std,
    }

    try:
        data = sorted(args)
    except TypeError:
        data = []
    
    for name in kwargs.values():
        handler = states.get(name) if isinstance(name, str) else None
        if handler is None:
            continue
        if not data:
            print("ERROR")
            continue
        try:
            print(f"{name} : {handler(data)}")
        except (TypeError, ValueError, ZeroDivisionError):
                print("ERROR")