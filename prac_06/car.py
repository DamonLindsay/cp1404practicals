"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    # Mod 6: Now add a name field to the Car class (in car.py), and adjust the __init__ and __str__ methods to set and
    # display this respectively.
    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    # Mod 5: Now add the __str__ method to the Car class in car.py.
    # Using f-string formatting. Make it return a string in the following format:
    # Car, fuel=42, odometer=277
    # Mod 6: Make the str method return the car's name instead of just "Car".
    def __str__(self):
        """Return the string version of the Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance
