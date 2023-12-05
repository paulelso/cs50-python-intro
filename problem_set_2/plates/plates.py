
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Plate must start with at least two letters.
    if len(s) < 2 or len(s) > 6:
        return False

    # First two character must be letters
    if not s[:2].isalpha():
        return False

    # Find first digit.
    match = re.search(r'\d', s)
    if match is not None:
        # The first number used cannot be a ‘0’.
        if match.group() == '0':
            return False
        # Numbers cannot be used in the middle of a plate; they must come at the end.
        if not s[match.start():].isnumeric():
            return False

    return True

if __name__ == "__main__":
    main()