"""
My Guitars
Expected Time: 60 minutes (3:33pm start)
Actual Time: 31 minutes (4:04pm finish)
"""

from guitar import Guitar
from operator import itemgetter

FILENAME = "guitars.csv"


def main():
    """This program will read all guitars in a CSV file and display them in a list."""
    guitars = []
    get_guitar(guitars)

    read_guitars_from_file(guitars)
    guitars.sort()
    display_guitars(guitars)

    write_to_file(guitars)


def get_guitar(guitars):
    """Get input from the user until they enter nothing."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        print()
        name = input("Name: ")


def read_guitars_from_file(guitars):
    """Get a list of guitars from the specified file."""
    with open(FILENAME, "r", encoding="utf-8") as input_file:
        for line in input_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)


def display_guitars(guitars):
    """Print each guitar in the list."""
    for guitar in guitars:
        print(guitar)


def write_to_file(guitars):
    """Write the guitars to the specified file."""
    with open(FILENAME, "w", encoding="utf-8") as output_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=output_file)


main()
