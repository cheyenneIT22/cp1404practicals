"""
CP1404, Prac_09,
Silver service taxi client program.
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

silver_taxi_1 = SilverServiceTaxi("Hummer", 100, 2)
silver_taxi_1.drive(18)
print(silver_taxi_1)
print("Fare: ${:.2f}".format(silver_taxi_1.get_fare()))
