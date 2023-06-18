"""do it from scratch exercises~ menu """
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
name = input("Enter your name: ")
choice = input("Choice:  ").lower()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Choice:  ").lower()
print("Finished.")