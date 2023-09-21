"""
Password Stars
"""
MINIMUM_PASSWORD_LENGTH = 5


def main():
    """This program will get a password from the user, and then print a number of *'s equal to the passwords length."""
    password = get_password()

    print_stars(password)


def print_stars(password):
    """Print a number of *'s matching the length of the given argument."""
    for character in range(len(password)):
        print("*", end="")


def get_password():
    """Get a valid password from the user."""
    password = input("Enter a password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid password.")
        password = input("Enter a password: ")
    return password


main()
