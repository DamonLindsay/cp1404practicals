"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Mod 1: Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Limo", 100)
    # Mod 2: Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
    # Mod 3: Print the amount of fuel in the car.
    print(f"Limo has fuel: {limo.fuel}")
    # Mod 4: Attempt to drive the car 115 km using the drive method.
    limo.drive(115)
    # Mod 7: In your used_cars.py program, print your car object/s to make sure that the __str__ method is working
    # as expected.
    print(limo)


main()
