MENU = "Welcome to the Star Game!"
print(MENU)
score = input("Enter your score: ")
choice = input("Choice:  ")
while choice != 0:
    if choice == 100:
        print("Valid score")
    elif choice == 50:
        print("Invalid Score")
print(MENU)
print(f"based of your {score} you get stars")
choice = input("Choice: ")
print("quit.")
