import re

def main():
    total = 0.0
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        try:
            item = get_item()
            total += menu.get(item, 0)
        # Ignore any input that isn’t an item, by reprompting
        except KeyError:
            item = get_item()
        # End program input with <Ctrl+D>
        except EOFError:
            exit(0)

        print(f"Total: ${total:.2f}")


def get_item():
    s = input("Item: ")
    # Return input in titlecase format
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                    lambda mo: mo.group(0).capitalize(), s)


if __name__ == "__main__":
    main()