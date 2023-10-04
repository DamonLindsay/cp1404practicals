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


def get_list_of_numbers(numbers):
    """Get a list of numbers."""
    for i in range(NUMBER_OF_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)


main()
