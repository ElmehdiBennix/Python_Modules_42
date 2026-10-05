def slice_me(family: list, start: int, end: int) -> list:
    """test"""

    if not isinstance(family, list):
        raise TypeError("Error: wrong type value family should be a list")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Error: wrong type value start or end should be a int")

    size = 0

    if len(family) > 0:
        lenght = None

        for idx, row in enumerate(family):
            if not isinstance(row, list):
                raise TypeError(
                    f"Error: wrong type value at index {idx} should be a list"
                )

            if lenght == None:
                lenght = len(row)
            elif len(row) != lenght:
                raise ValueError("Error: lenght of the arrays dont match")

        size = lenght

    print(f"My shape is : ({len(family)}, {size})")

    sliced_family = family[start:end]

    sliced_family_lenght = len(sliced_family[0]) if (len(sliced_family) > 0) else 0

    print(f"My new shape is :({len(sliced_family)}, {sliced_family_lenght})")

    return sliced_family


family = [[1.50, 75.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.21]]


print(slice_me(family, 0, 2))

print(slice_me(family, 1, -2))
