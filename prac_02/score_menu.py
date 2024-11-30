import random

MENU = """G -Get Valid Score\n P - Print Result \n Q - Quit \n>>> """
def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            result = get_valid_score(score)
            print(result)
        elif choice == "P":
            score = random.randint(0, 100)
            result = determine_result(score)
            print(f"Random Score:  - Result: ".format(score, result))
        elif choice == "S":
            score = int(input("Enter score (number of stars): "))
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
    choice = input(">>> ").upper()


print("Farewell.")


def get_valid_score(score):
    score = random.randint(0, 100)
    result = determine_result(score)
    return result


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


def print_stars(score):
    print("Star Rating: " + "*" * score)
