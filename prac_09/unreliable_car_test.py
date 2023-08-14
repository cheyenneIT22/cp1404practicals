"""UnreliableCar Tests."""
from prac_09.unreliable_car import UnreliableCar


def main():
    working_car = UnreliableCar("Mostly good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)


for i in range(1, 12):
    print(f"Attempting to drive {i}km: ")
    print(f"{working_car.name: 12} drove {working_car.drive(i):2}km")
    print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

print(working_car)
print(bad_car)
main()
