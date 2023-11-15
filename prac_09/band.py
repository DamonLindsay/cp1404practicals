"""
Band class module
Estimated: 30 minutes
Actual: 43 minutes
"""

from prac_09.musician import Musician


class Band:
    """Band class for storing details of a Band."""

    def __init__(self, name=""):
        """Initialize a Band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)
