"""
Sequences
"""


def main():
    """This menu-based program will take two integers from the user and then provide
    options with what to do with them."""
    first_number = int(input("Enter first number (This will be X): "))
    second_number = int(input("Enter second number (This will be Y: "))

    MENU = (f"(E)ven Numbers from {first_number} to {second_number}\n"
            f"(O)dd Numbers from {first_number} to {second_number}\n"
            f"(S)quares from {first_number} to {second_number}\n"
            "(Q)uit")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "e":
            print(f"Even numbers between {first_number} and {second_number}.")
            if first_number % 2 == 0:
                for i in range(first_number, second_number + 1, 2):
                    print(i, end=" ")
                print()
            else:
                for i in range(first_number + 1, second_number + 1, 2):
                    print(i, end=" ")
                print()

        elif choice == "o":
            print(f"Odd numbers between {first_number} and {second_number}.")
            if first_number % 2 == 1:
                for i in range(first_number, second_number + 1, 2):
                    print(i, end=" ")
                print()
            else:
                for i in range(first_number + 1, second_number + 1, 2):
                    print(i, end=" ")
                print()

        elif choice == "s":
            print(f"Squares between {first_number} and {second_number}.")
            for i in range(first_number, second_number + 1):
                square = i ** 2
                print(square, end=" ")
            print()

        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").lower()


main()
