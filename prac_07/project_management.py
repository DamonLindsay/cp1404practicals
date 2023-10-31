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
            filename = input("Enter Filename: ")
            save_projects_to_file(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("Filter projects by date")
        elif choice == "A":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option.")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def read_project_from_file(projects, filename):
    """Read project information from a file and populate a list of projects."""
    with open(filename, "r", encoding="utf-8") as input_file:
        for line in input_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost = float(parts[3])
            percentage_completion = int(parts[4])
            project = Project(name, start_date, priority, cost, percentage_completion)
            projects.append(project)


def save_projects_to_file(projects, filename):
    """Save the projects to a specified file."""
    with open(filename, "w", encoding="utf-8") as output_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=output_file)


def display_projects(projects):
    """Display all projects in the current list."""
    sorted_projects = projects
    sorted_projects.sort()
    display_incomplete_projects(sorted_projects)
    display_completed_projects(sorted_projects)


def display_incomplete_projects(projects):
    """Display incomplete projects."""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 100:
            print(f"  {project}")


def display_completed_projects(projects):
    """Display completed projects."""
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(f"  {project}")


def add_project(projects):
    """Add a new project (from user input) to the specified list."""
    project_name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    projects.append(Project(project_name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    """Update the specified project based on user input."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])

    new_percentage = int(input("New Percentage: "))
    projects[project_choice].completion_percentage = new_percentage

    new_priority = int(input("New Priority: "))
    projects[project_choice].priority = new_priority


main()
