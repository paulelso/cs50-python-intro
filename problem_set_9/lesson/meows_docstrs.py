def main():
    num = int(input("Number: "))
    meows = meow(num)
    print(meows, end="")

def meow(n):
    """
    Meow n times
    
    :param n: number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :raise ValueError: if n is not positive
    :return: a string of n meows, one per line
    :rtype: str    
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
        exit(1)
    if n < 1:
        raise ValueError("n must be positive")
        exit(1)
    return "meow\n" * n

if __name__ == "__main__":
    main()