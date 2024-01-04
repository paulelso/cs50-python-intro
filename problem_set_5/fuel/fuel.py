def main():
    gauge(convert(input("Fraction: ")))


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split('/'))
            if y == 0 or x > y:
                main()
            try:
                percentage = (x / y) * 100
                return percentage
            except ZeroDivisionError:
                exit(1)
        except (NameError, ValueError):
            main()


def gauge(percentage):
    if percentage <= 1:
        print("E")
    # If 99% or more remains, output F
    elif percentage >= 99:
        print("F")
    else:
        # Percentage rounded to the nearest integer.
        print(f"{round(percentage)}%")


if __name__ == "__main__":
    main()
