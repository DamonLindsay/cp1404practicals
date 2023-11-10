"""
Guitar class module
"""
CURRENT_YEAR = 2023


class Guitar:
    """Guitar class module"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize the Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string version of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return 'True' if the guitar is 50 or more years old."""
        if Guitar.get_age(self) > 50:
            return True
        else:
            return False

