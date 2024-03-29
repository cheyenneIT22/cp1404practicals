"""
CP1404/CP5632 Practical
Total Income Cumulative program
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income: {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income:  ${income:10.2f}total: ${total:10.2f}")


main()
