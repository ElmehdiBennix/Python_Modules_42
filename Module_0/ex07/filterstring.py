"""Print the words of a string that are longer than an integer."""

import sys


def main():
    """Filter sys.argv words by length and print the result."""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    result = [
        w for w in sys.argv[1].split() if (lambda x: len(x) > n)(w)
    ]
    print(result)


if __name__ == "__main__":
    main()
