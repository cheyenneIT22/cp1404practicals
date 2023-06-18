"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
"""
sales = float(input("Enter sales: $"))
if sales >= 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15

print("Bonus is $", bonus, sep="")
