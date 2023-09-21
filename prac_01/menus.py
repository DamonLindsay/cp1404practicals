"""
Menus Program

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""


def get_input(prompt):
    """Takes a prompt as an argument and returns the input as a string."""
    user_input = input(prompt)
    return user_input


def display_menu_options():
    """Display the options in the menu."""
    print("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit")


def menu(name, choice):
    """Runs through the menu options, returning the users choice."""
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice.")
        display_menu_options()
        choice = get_input(">>> ").upper()
    return choice


def main():
    """This program asks for a users name and then provides a list of options."""
    name = get_input("Enter name: ")
    display_menu_options()
    choice = get_input(">>> ").upper()
    while choice != "Q":
        choice = menu(name, choice)
    print("Finished.")


main()
