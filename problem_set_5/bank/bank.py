import re

def main():
    print(f"${value(input('Input: '))}")

def value(greeting):
    # Remove leading whitespace and convert to lowercase
    greeting = greeting.lstrip().lower()
    # If the greeting starts with “hello”, output $0.
    if re.match("hello", greeting):
        value = int(0)
    # If the greeting starts with an “h” (but not “hello”), output $20.
    elif re.match("h", greeting):
        value = int(20)
    # Otherwise, output $100
    else:
        value = int(100)

    return value

if __name__ == '__main__':
    main()