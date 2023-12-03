amount_due = 50
total_inserted = 0

while total_inserted < amount_due:
    print(f"Amount Due: {amount_due - total_inserted}")
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        total_inserted += coin

change = abs(amount_due - total_inserted)
print(f"Change Owed: {change}")