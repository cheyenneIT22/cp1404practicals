"""do it from scratch exercises~ Menus
 Pseudocode:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message """

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
