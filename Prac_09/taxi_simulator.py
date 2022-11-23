"""Taxi Simulator"""
from Prac_09.car import car
from Prac_09.taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main function that uses both Taxi and SilverServiceTaxi program"""
    total_bill = None
    print("Lets Drove!")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis Available")
            display_taxis(Taxi)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = Taxi[Taxi]
            except IndexError:
                print("Invalid Taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(Taxi)


def display_taxis(taxis):
    """Displays numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def run_tests():
    """Runs tests to show workings of Car and Taxi classes."""
    bus = car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus._odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus._odometer)
    print(bus)

    distance = int(input("Drive how far? "))
    while distance > 0:
        distance_travelled = bus.drive(distance)
        print(f"{bus} travelled {distance_travelled}")
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()
