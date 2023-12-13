# Initialize an empty dictionary to store the items and their counts
grocery_list = {}

try:
    while True:
        item = input()
        # If the item is already in the dictionary, increment its  count
        if item in grocery_list:
            grocery_list[item] += 1
         # Otherwise add the tiem to the dictionary with a count of 1
        else:
            grocery_list[item] = 1
# Handle the end of input <CTRL+D>
except EOFError:
    # Sort the list alphabetically
    sorted_list = dict(sorted(grocery_list.items()))
    for keys, value in sorted_list.items():
        # Output the list in all uppercase prefixed by the number of
        # times an item was inputted
        print(f"{value} {keys.upper()}")
    exit(0)