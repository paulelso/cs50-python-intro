def get_fraction():
    while True:
        # If X or Y is not an integer, prompt the user again.
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))
            return x, y
        except (NameError, ValueError):
            get_fraction()


def is_valid(x, y):
    if y == 0 or x > y:
        return False

    return True


def get_fuel(x, y):
    while True:
        try:
            percentage = (x / y) * 100
            # If 1% or less remains, output E
            if percentage <= 1:
                print("E")
            # If 99% or more remains, output F
            elif percentage >= 99:
                print("F")
            else:
                # Percentage rounded to the nearest integer.
                print(f"{round(percentage)}%")

        except ZeroDivisionError:
            get_fraction()

        else:
            break


def main():
    while True:
        x, y = get_fraction()
        # If X is greater than Y, or Y is 0, prompt the user again.
        if is_valid(x, y):
            get_fuel(x, y)
            break


if __name__ == "__main__":
    main()