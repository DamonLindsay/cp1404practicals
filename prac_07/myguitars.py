"""
My Guitars
Expected Time: 60 mins (3:33pm start)
Actual Time:
"""

from guitar import Guitar
from operator import itemgetter

FILENAME = "guitars.csv"


def main():
    """This program will read all guitars in a CSV file and display them in a list."""
    guitars = []
    get_guitars(guitars)

    guitars.sort()

    display_guitars(guitars)


def display_guitars(guitars):
    """Print each guitar in the list."""
    for guitar in guitars:
        print(guitar)


def get_guitars(guitars):
    """Get a list of guitars from the specified file. """
    with open(FILENAME, "r", encoding="utf-8") as output_file:
        for line in output_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)


main()
