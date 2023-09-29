"""
ASCII Table - Extension
"""

MINIMUM_NUMBER_VALUE = 33
MAXIMUM_NUMBER_VALUE = 127


def main():
    """This program will take a character input and see the corresponding ASCII code, and vice versa."""
    character = get_valid_character()
    print(f"The ASCII code for '{character}' is '{ord(character)}'.")

    user_number = get_valid_number(MINIMUM_NUMBER_VALUE, MAXIMUM_NUMBER_VALUE)
    print(f"The character for '{user_number}' is '{chr(user_number)}'.")


def get_valid_character():
    """Get a valid character as an input."""
    is_valid_character = False
    while not is_valid_character:
        character = input("Enter a character: ")
        if len(character) < 1 or len(character) > 1:
            print("Invalid input.  Only a single character must be entered.")
        elif character.isalpha():
            is_valid_character = True
        else:
            is_valid_character = True
    return character


def get_valid_number(minimum, maximum):
    """Take input for a number, checking it is between the minimum and maximum values inclusive."""
    user_number = int(input(f"Enter a number between {minimum} and {maximum}: "))
    while user_number < minimum or user_number > maximum:
        print("Invalid number.")
        user_number = int(input(f"Enter a number between {minimum} and {maximum}: "))
    return user_number


main()
