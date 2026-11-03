"""Limit how many times a decorated function is allowed to run."""

from typing import Any


def callLimit(limit: int):
    """Return a decorator allowing at most limit calls to a function."""
    count = 0

    def callLimiter(function):
        """Wrap function with the counter owned by this factory call."""

        def limit_function(*args: Any, **kwds: Any):
            """Run function while the allowance lasts, else print an error."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
