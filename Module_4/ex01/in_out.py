
def square(x: int | float) -> int | float:
    if not isinstance(x, int | float) or isinstance(x, bool):
        raise TypeError("Error")
    return x ** 2
    
def pow(x: int | float) -> int | float:
    if not isinstance(x, int | float) or isinstance(x, bool):
        raise TypeError("Error")
    return x ** x

def outer(x: int | float, function) -> object:
    if not isinstance(x, int | float) or isinstance(x, bool):
        raise TypeError("Error")
    
    count = 0
    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner