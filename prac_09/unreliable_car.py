"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from random import randint
from prac_09 import car
class UnreliableCar(car):
    """Unreliable car that inherits from Car."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
    def __str__(self):
        return "{} reliability={}".format(super().__str__(), self.reliability)


 def drive(self, distance):
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
