"""
Guitar class module
"""
CURRENT_YEAR = 2023


class Guitar:
    """Guitar class module"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialize the Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string version of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __repr__(self):
        """Return the string version of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Determine if the current year is less than the other year attribute."""
        return self.year < other.year

    def __gt__(self, other):
        """Determine if the current year is greater than the other year attribute."""
        return self.year > other.year

    def __eq__(self, other):
        """Determine if the current year is equal to the other year attribute."""
        return self.year == other.year

    def get_age(self):
        """Return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return 'True' if the guitar is 50 or more years old."""
        return self.get_age() >= 50
