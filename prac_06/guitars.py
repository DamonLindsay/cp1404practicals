"""
Expected Finish Time: 30 minutes (4:47pm start)
Actual Finish Time: 44 minutes (5:31pm finish)
"""

from prac_06.guitar import Guitar


def main():
    """This program will store all the user's guitars, then print their details."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        print()
        name = input("Name: ")

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() is True else ""

        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
