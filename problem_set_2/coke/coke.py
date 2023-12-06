amount_due = 50
total_inserted = 0

while total_inserted < amount_due:
    print(f"Amount Due: {amount_due - total_inserted}")
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        total_inserted += coin

change = abs(amount_due - total_inserted)
print(f"Change Owed: {change}")