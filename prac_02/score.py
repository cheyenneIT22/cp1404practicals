"""
Broken program to determine score status
(FIXED CODE)
"""
import random


def determine_result(score):
    if score < 0 or score > 100:
        if score > 100:
            print("Invalid score")
        elif score > 50:
            print("Passable")
        elif score > 90:
            print("Excellent")
        else:
            print("bad")


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    # Gets random score and prints the result.
    score = random.randint(0, 100)
    result = determine_result(score)
    print(f"Random Score:  - Result: ".format(score, result))
