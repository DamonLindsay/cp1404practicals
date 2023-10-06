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

    repeated_words = return_repeated_words(strings)

    print(f"Strings repeated: {repeated_words}")


def return_repeated_words(strings):
    """Find any words repeated more than once in a list and return a new list containing the repeated words."""
    repeated_words = []
    for string in strings:
        if strings.count(string) > 1:
            repeated_words.append(string)

    return repeated_words


main()
