import mypy

def main():
    number = input("Number: ")
    meow(number)

def meow(n):
      for _ in range(n):
          print("meow")

if __name__ == "__main__":
    main()