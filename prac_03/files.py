"""
Files - Prac 03
"""
NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"


def main():
    """This program contains questions 1-4."""
    # Question 1
    write_name_to_file(NAME_FILE)

    # Question 2
    print_from_file(NAME_FILE)

    # Question 3
    total = add_first_two_numbers_from_file(NUMBERS_FILE)
    print(total)

    # Question 4
    total = add_all_numbers_from_file(NUMBERS_FILE)
    print(total)


def write_name_to_file(filename):  # Question 1
    """Write the users name to the specified file."""
    name = input("Name: ")

    with open(filename, "w") as out_file:
        print(f"{name}", file=out_file)


def print_from_file(filename):  # Question 2
    """Print the name from the specified file."""
    with open(filename, "r") as in_file:
        name = in_file.read().strip()
        print(f"Your name is {name}.")


def add_first_two_numbers_from_file(filename):  # Question 3
    """Take the first two numbers from a specified file, add them and then return the total."""
    with open(filename, "r") as in_file:
        first_number = int(in_file.readline().strip())
        second_number = int(in_file.readline().strip())
        total = first_number + second_number
        return total


def add_all_numbers_from_file(filename):  # Question 4
    """Add all numbers from a specified file, then return the combined total."""
    total = 0
    with open(filename, "r") as in_file:
        for line in in_file:
            number = int(line.strip())
            total += number
        return total
