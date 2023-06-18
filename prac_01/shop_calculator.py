"""do-from-scratch exercises-shop calculator"""
total = 0
item = int(input("number of items: "))
while item < total:
    print("Invalid number of items.")
    item = int(input("number of items: "))
for i in range(item):
    item_price = float(input("Price of item: "))
    total += item_price
if item_price > 100:
    item_price *= 0.9
print("Total price for", "items is $", total, sep="")
print(f"Total price for {item} items is ${item_price:.2f}")
