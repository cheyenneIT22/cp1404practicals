"""Secret Password program."""
MINIMUM_LENGTH = 5


def first_name():
    """displays password user enters"""
    password_name = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password_name) < MINIMUM_LENGTH:
        password_name = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
        print('*' * len(password_name))


def main():
    """main function of program and displays the password"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    """determines the length of password based of number of characters"""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("password is too short.")
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    return password


def print_asterisks(sequence):
    """prints the password as asterisks sequence"""
    print('*' * len(sequence))


main()
