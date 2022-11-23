"""SilverService Taxi class, Derived from Taxi program."""
from Prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    FlagFall = 4.5


def __init__(self, name, fuel, fanciness):
    super().__init__(name, fuel)
    self.fanciness = fanciness
    self.price_per_km *= fanciness


def __str__(self):
    return f"{super().__str__()} plus FlagFall of ${self.FlagFall:.2f}"


def get_fare(self):
    return self.FlagFall + super().get_fare()
