"""CP1404/CP5632,Prac09,
Client code for taxi class program"""
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
print(my_taxi)
my_taxi.drive(40)
print(f"Current Fare $: {my_taxi.current_fare_distance:2f}$")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Current Fare: {my_taxi.current_fare_distance:2f}$")
print(my_taxi)
