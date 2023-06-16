"""Temperature conversions."""
MENU = """C - convert celsius to fahrenheight, F- convert fahrenheight to celsius, Q- quit"""
def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
