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

    repeated_words = find_repeated_items(strings)

    print(f"Strings repeated: {repeated_words}")


def find_repeated_items(items):
    """Find any words repeated more than once in a list and return a new list containing the repeated words."""
    repeated_items = []
    for item in items:
        if items.count(item) > 1:
            repeated_items.append(item)

    return repeated_items


# main()

print(find_repeated_items([1, 2, 3, 3, 1, 5, 1]))
