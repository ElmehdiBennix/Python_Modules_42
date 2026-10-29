"""Count upper-case, lower-case, punctuation, space and digit characters."""

import sys


def main():
    """Count and report the character classes of the given text."""
    length = len(sys.argv)

    if length > 2:
        print("AssertionError: more than one argument is provided")
        return
    if length == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        text = sys.stdin.read()

    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isnumeric():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
