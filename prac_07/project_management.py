"""
Project Management
Expected Time: 120 minutes (8:03pm start)
Actual Time:
"""

from project import Project
import datetime

DEFAULT_FILENAME = "projects.txt"
MENU_INSTRUCTIONS = (
    "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
    "- (U)pdate project\n- (Q)uit")


def main():
    """This menu-based program will allow a user to interact with various projects and check their status,
    as well as update them. """
    projects = []

    read_project_from_file(projects, DEFAULT_FILENAME)

    print(MENU_INSTRUCTIONS)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter Filename: ")
            read_project_from_file(projects, filename)
        elif choice == "S":
            print("Save projects")
        elif choice == "D":
            display_projects(projects)
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


def read_project_from_file(projects, filename):
    """Read project information from a file and populate a list of projects."""
    with open(filename, "r", encoding="utf-8") as input_file:
        input_file.readline()
        for line in input_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost = float(parts[3])
            percentage_completion = int(parts[4])
            project = Project(name, start_date, priority, cost, percentage_completion)
            projects.append(project)


def display_projects(projects):
    """Display all projects in the current list."""
    print("Incomplete projects:")
    for project in projects:
        print(f"  {project}")


main()
