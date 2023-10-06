"""
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

    Each line (quick pick) should not contain any repeated number.
    Each line of numbers should be displayed in sorted (ascending) order.
    Study the formatting below so that numbers align neatly.
"""
import random

NUMBER_OF_NUMBERS_PER_QUICK_PICK = 6
LOWEST_RANDOM_NUMBER = 1
HIGHEST_RANDOM_NUMBER = 45


def main():
    """This program will ask the user how many 'quick picks' to generate, then generates that many lines out output."""
    number_of_quick_picks = int(input("How many quick picks? "))
    print_quick_pick(number_of_quick_picks)


def print_quick_pick(number_of_quick_picks):
    """Print the quick pick."""
    for i in range(number_of_quick_picks):
        quick_picks = generate_quick_pick(NUMBER_OF_NUMBERS_PER_QUICK_PICK, LOWEST_RANDOM_NUMBER, HIGHEST_RANDOM_NUMBER)
        quick_picks.sort()
        for quick_pick in quick_picks:
            print(f"{quick_pick:2}", end=" ")
        print()


def generate_quick_pick(number_of_numbers, lowest_value, highest_value):
    """Generate a list of quick picks between a low and high value."""
    return [random.randint(lowest_value, highest_value) for i in range(number_of_numbers)]


main()
