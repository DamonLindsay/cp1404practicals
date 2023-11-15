"""
Silver Service Taxi Class Module
Estimate: 20 minutes
Actual: 23 Minutes
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name="", fuel=0, fanciness=0.0):
        """Initialize the Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * Taxi.price_per_km
        self.current_fare_distance = 0

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + (self.price_per_km * self.current_fare_distance)

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
