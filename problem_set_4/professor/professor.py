import random

def main():
    generate_integer(get_level())

def get_level():
    try:
        level = int(input("Level: "))
        if level not in [1, 2, 3]:
            raise ValueError(get_level())
    except ValueError:
        get_level()
    return level

def generate_integer(level):
    score = 0
    if level == 1:
        rangex = 0
        rangey = 10
    elif level == 2:
        rangex = 10
        rangey = 100
    elif level == 3:
        rangex = 100
        rangey = 1000
    for i in range(10):
        x = random.randrange(rangex, rangey)
        y = random.randrange(rangex, rangey)
        try:
            count = 0
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                score += 1
            else:
                print("EEE")
                while answer != (x + y):
                    count += 1
                    if count == 3:
                        print(f"Answer: {x + y}")
                        break
                    else:
                        answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
    print(f"Score: {score}")

if __name__ == "__main__":
    main()