"""
Unreliable Car Class Module
Estimated: 15 minutes
Actual:
"""
import random

from prac_06.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name="", fuel=0, reliability=0.0):
        """Initialize an Unreliable Car object."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but use reliability to determine the chance this method works."""
        if random.randint(0, 100) < self.reliability:
            return 0
        distance_driven = super().drive(distance)
        return distance_driven
