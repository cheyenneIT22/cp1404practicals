"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
# result = 0
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        result = int(input("Enter a valid integer: "))
        print("Please enter a valid integer.")
        print("Valid result is: ", result)

