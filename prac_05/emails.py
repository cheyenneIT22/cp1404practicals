"""Emails program."""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
    confirmation = input(f"is your name {name}? (Y/N?)")
    if confirmation.upper() != "Y" and confirmation != "":
        name = input("Name")
        email = input("Email: ")


for email, name in email_to_name.items():
    print(f"{name},{email}")


def get_name_from_email(email):
    """Extract from email input"""


prefix = email.split('@')[0]
parts = prefix.split('.')
name = "".join(parts).title()
return name