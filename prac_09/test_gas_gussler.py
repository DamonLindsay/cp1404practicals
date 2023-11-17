"""
Extension - Gas Gussler
Test Gas Gussler class module
"""
from prac_09.gas_gussler import GasGussler


def main():
    """Run tests."""
    test_car = GasGussler(name="GasGussler", fuel=100)
    print("Initial car.")
    print(test_car)
    test_car.drive(20)
    print()
    print("Car should have driven 20km, and used twice as much fuel (40).")
    print(test_car)


main()
