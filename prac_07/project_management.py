"""
Project Management
Expected Time: 120 minutes (8:03pm start)
Actual Time:
"""

from project import Project

MENU_INSTRUCTIONS = (
    "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
    "- (U)pdate project\n- (Q)uit")


def main():
    """This menu-based program will allow a user to interact with various projects and check their status,
    as well as update them. """
    print(MENU_INSTRUCTIONS)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Load projects")
        elif choice == "S":
            print("Save projects")
        elif choice == "D":
            print("Display projects")
        elif choice == "F":
            print("Filter projects by date")
        elif choice == "A":
            print("Add new project")
        elif choice == "U":
            print("Update project")
        else:
            print("Invalid option.")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


main()

# print(Project("Build Car Park", "12/09/2021", 2, 60000.0, 95))
