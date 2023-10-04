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


def get_list_of_numbers(numbers):
    """Get a list of numbers."""
    for i in range(NUMBER_OF_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)


main()
