"""Emails program."""


def main():
    email_to_name = {}
    personal_email = input("Email: ")
    while personal_email != "":
        name = get_name_from_email()
    confirmation = input(f"is your name {name}? (Y/N?)")
    if confirmation.upper() != "Y" and confirmation != "":
        email_name = input("Name:")
        email_to_name[personal_email] = name
        personal_email = input("Email: ")


for email, name in email_to_name.items():
    print(f"{name},{email}")


def get_name_from_email():
    """Extract from email input"""


prefix = email.split('@')[0]
parts = prefix.split('.')
name = "".join(parts).title()
return name


main()