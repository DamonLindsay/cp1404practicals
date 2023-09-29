"""
Random Things - Extension
"""

import random


def main():
    """This program will generate a random Boolean in 3 different ways."""
    random_number = random.randint(1, 2)
    print(random_number == 1)

    print(random.choice([True, False]))

    print(bool(random.getrandbits(1)))


main
