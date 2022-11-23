"""generating a random score"""
import random


def main():
    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid score")
    else:
        print(score)


def random_score(score):
    if score > 100:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")


print(random_score)
main()
