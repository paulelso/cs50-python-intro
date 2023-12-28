import inflect
names = []
p = inflect.engine()
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}")
        elif len(names) > 1:
            mylist = p.join(names, sep=",")
            print(f"Adieu, adieu, to {mylist}")
        exit(0)