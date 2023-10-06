"""
String Repeater - Practice
"""


def main():
    """This program will ask the user for an indefinite set of strings - until an empty string
     is entered - then prints all the strings that were entered more than once."""
    strings = []

    user_string = input("Enter a string: ")
    while user_string != "":
        strings.append(user_string)
        user_string = input("Enter a string: ")


main()
