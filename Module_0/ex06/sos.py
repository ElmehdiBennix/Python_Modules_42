"""Encode a command-line string into Morse code."""

import sys


def main():
    """Encode the argument string into Morse code."""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    text = sys.argv[1].upper()
    for char in text:
        if char not in NESTED_MORSE:
            print("AssertionError: the arguments are bad")
            return

    print("".join(NESTED_MORSE[char] for char in text).rstrip())


if __name__ == "__main__":
    main()
