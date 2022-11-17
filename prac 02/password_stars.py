"""Secret password"""


def main():
    password_check = user_password()
    return password_check
def user_password(password_check):
    numerics = "013456789"
    capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_character = "@#"
while len (user_password) != 6:
    user_password = input("Enter a valid username: ")
    print(user_password)

