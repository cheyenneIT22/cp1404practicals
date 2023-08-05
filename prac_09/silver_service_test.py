"""SilverServiceTaxi class tests"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """CLient testing code for SilverServiceTaxi program."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())
