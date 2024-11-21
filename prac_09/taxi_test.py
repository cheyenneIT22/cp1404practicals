"""CP1404,Prac09,
Client code for taxi class program"""
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
print(my_taxi)
distance_driven = my_taxi.drive(40)
print(f"Distance driven: {distance_driven} km")
print(f"Current Fare: {my_taxi.current_fare_distance:2f}$")
my_taxi.start_fare()
distance_driven = my_taxi.drive(100)
print(f"Distance driven: {distance_driven} km")
print(f"Current Fare: {my_taxi.current_fare_distance:2f}$")
