"""Square, exponentiate, and compound a value through a callable."""

from collections.abc import Callable


def square(x: float) -> int | float:
    """Return x squared, rejecting non-numbers and booleans."""
    if not isinstance(x, int | float) or isinstance(x, bool):
        raise TypeError("Error")
    return x**2


def pow(x: float) -> int | float:
    """Return x raised to its own power, rejecting non-numbers."""
    if not isinstance(x, int | float) or isinstance(x, bool):
        raise TypeError("Error")
    return x**x


def outer(
    x: float, function: Callable[[int | float], int | float]
) -> Callable[[], float]:
    """Return a callable compounding function on the latest value."""
    if not isinstance(x, int | float) or isinstance(x, bool):
        raise TypeError("Error")

    count = x

    def inner() -> float:
        """Apply function to the stored value and return the result."""
        nonlocal count
        count = function(count)
        return count

    return inner
