"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. the ValueError occurs when the user types in a value that is not valid or a value that could break the code.
# 2. an ZeroDivisionError occurs when the Value the user enters is not divisible by 0 and breaks the code.
# 3. I could change the code by to prevent an ZeroDivisionError error by adding specific values the user can enter.
