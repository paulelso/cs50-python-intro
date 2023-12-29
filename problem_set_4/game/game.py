import random

def main():
    level = get_level()
    guess = get_guess()
    get_answer(level, guess)

def get_level():
    try:
        level = int(input("Level: "))
        if level <= 0:
            get_level()
        else:
            return level
    except ValueError:
        get_level()

def get_guess():
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            get_guess()
        else:
            return guess
    except ValueError:
        get_guess()

def get_answer(level, guess):
    num = random.randrange(1, level + 1)
    while guess != num:
        if guess < num:
            print("Too small!")
            guess = get_guess()
        elif guess > num:
            print("Too large!")
            guess = get_guess()
    print("Just right!")
    return

if __name__ == "__main__":
    main()