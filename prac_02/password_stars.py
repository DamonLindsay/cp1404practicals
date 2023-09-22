"""
Password Stars
"""
MINIMUM_PASSWORD_LENGTH = 5


def main():
    """This program will get a password from the user, and then print a number of *'s equal to the
    password's length."""
    password = get_password(MINIMUM_PASSWORD_LENGTH)

    print_stars(password)


def print_stars(password):
    """Print a number of *'s matching the length of the given password."""
    print("*" * len(password))


def get_password(minimum_length):
    """Get a valid password from the user."""
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Invalid password.")
        password = input("Enter a password: ")
    return password


main()
