"""
List Exercises - Prac -04
"""
NUMBER_OF_NUMBERS = 5


def main():
    """This program prompts the use for numbers, then outputs information about these numbers."""
    numbers = []
    get_list_of_numbers(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")
    validate_username(username, usernames)


def get_list_of_numbers(numbers):
    """Get a list of numbers."""
    number = int(input(f"Number {len(numbers) + 1}: "))
    while number != 0:
        numbers.append(number)
        number = int(input(f"Number {len(numbers) + 1}: "))


def validate_username(username, usernames):
    """Check if the username is in the list of usernames."""
    if username in usernames:
        print("Access granted.")
    else:
        print("Access denied.")


main()
