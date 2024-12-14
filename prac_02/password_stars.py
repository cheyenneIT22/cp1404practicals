"""Secret Password program."""
MIN_LENGTH = 5


def main():
    """main function of program and displays the password"""
    password = get_password({MIN_LENGTH})
    print_asterisks(password)


def print_asterisks(sequence):
    """prints the password as asterisks sequence"""
    print('*' * len(sequence))


def get_password(MIN_LENGTH):
    """determines the length of password based of number of characters"""
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("password is too short.")
        password = input(f"Enter password of at least {MIN_LENGTH} characters: ")
    return password


main()
