"""SilverService Taxi class, Derived from Taxi program."""
from prac_09.Taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi"""
    FlagFall = 4.5


def __init__(self, name, fuel, fanciness):
    """Initialise a SilverServiceTaxi"""
    super().__init__(name, fuel)
    self.fanciness = fanciness
    self.price_per_km *= fanciness


def __str__(self):
    """Return a string representation of SilverServiceTaxi."""
    return f"{super().__str__()} plus FlagFall of ${self.FlagFall:.2f}"


def get_fare(self):
    """Get updated and current fare."""
    return self.FlagFall + super().get_fare()
