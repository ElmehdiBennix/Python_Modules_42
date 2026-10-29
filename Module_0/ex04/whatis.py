"""Report whether the single integer argument is even or odd."""

import sys


def main():
    """Print the parity of the integer given as the only argument."""
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
