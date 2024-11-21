"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_09 import car


class UnreliableCar(car):
    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
