"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""

from prac_06 import cars


def main():
    """Demo test code to show how to use car class."""
    limo = car(180)
    limo.drive(20)
    print(f"Car has fuel: {limo.fuel}")
    print(limo)


main()
