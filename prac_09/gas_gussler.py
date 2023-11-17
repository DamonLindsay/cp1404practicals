"""
Gas Gussler class module
"""

from taxi import Taxi


class GasGussler(Taxi):
    """Specialised version of a taxi that uses more fuel than it should."""

    def __init__(self, **kwargs):
        """Initialize the Gas Gussler object."""
        super().__init__(**kwargs)
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel * 2:
            distance = self.fuel * 2
            self.fuel = 0
        else:
            self.fuel -= distance * 2
        self._odometer += distance

        self.current_fare_distance += distance
        return distance

    def __str__(self):
        """Return a string version of the Gas Gussler object."""
        return super().__str__()

    def __repr__(self):
        """Return a debug version of the Gas Gussler object."""
        return f"GasGussler(name={self.name}, fuel={self.fuel})"
