"""
ASCII Table - Extension
"""

MINIMUM_NUMBER_VALUE = 33
MAXIMUM_NUMBER_VALUE = 127


def main():
    """This program will take a character input and see the corresponding ASCII code, and vice versa."""
    character = input("Enter a character: ")
    print(f"The ASCII code for {character} is {ord(character)}.")

    user_number = get_valid_number(MINIMUM_NUMBER_VALUE, MAXIMUM_NUMBER_VALUE)
    print(f"The character for {user_number} is {chr(user_number)}.")


def get_valid_number(minimum, maximum):
    """Take input for a number, checking it is between the minimum and maximum values inclusive."""
    user_number = int(input(f"Enter a number between {minimum} and {maximum}: "))
    while user_number < minimum or user_number > maximum:
        print("Invalid number.")
        user_number = int(input(f"Enter a number between {minimum} and {maximum}: "))
    return user_number


main()
