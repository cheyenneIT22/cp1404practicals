"""do-from-scratch exercises-shop calculator"""
DISCOUNT = 0.1
total = 0
number_of_items = int(input("number of items: "))
while number_of_items < 0:
    print("Invalid number of items.")
    number_of_items = int(input("number of items: "))
for i in range(number_of_items):
    total_price = float(input("Price of item: "))
    total += total_price
if total > 100:
    total = total - (total * DISCOUNT)
    print(f"Total price for {number_of_items}, is $ {total:.2f}")
