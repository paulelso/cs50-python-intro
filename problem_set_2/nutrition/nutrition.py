# Prompt the user to input a fruit
k = input("Item: ").lower()

# Dictionary mapping fruits to their calorie counts
d = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 60,
    "grapes": 90,
    "melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "necatrine": 60,
    "orange": 80,
    "peach" : 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# Print the selected fruit's calorie count
if k in d:
    print(f"Calories: {d[k]}")