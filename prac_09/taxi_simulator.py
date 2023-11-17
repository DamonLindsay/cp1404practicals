"""
Taxi Simulator Program
Estimated Time: 90 minutes
Actual Time:
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_INSTRUCTIONS = "q)uit, c)hoose, d)rive"


def main():
    """A Taxi Simulator program that """
    current_taxi = None
    current_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU_INSTRUCTIONS)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                current_bill += cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill:.2f}")
        print(MENU_INSTRUCTIONS)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${current_bill:.2f}")
    print(f"Taxis are now: ")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display a list of taxi's to select."""
    display_taxis(taxis)
    chosen_taxi_index = int(input("Choose taxi: "))
    if 0 <= chosen_taxi_index < len(taxis):
        return taxis[chosen_taxi_index]
    else:
        print("Invalid taxi choice")
        return None


def display_taxis(taxis):
    """Display the current list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
