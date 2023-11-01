"""
Project Management
Expected Time: 120 minutes (8:03pm start)
Actual Time:
"""

from project import Project
from datetime import datetime

DEFAULT_FILENAME = "projects.txt"
MENU_INSTRUCTIONS = (
    "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
    "- (U)pdate project\n- (Q)uit")


def main():
    """This menu-based program will allow a user to interact with various projects and check their status,
    as well as update them. """
    projects = []

    load_or_save_projects(projects, DEFAULT_FILENAME, "load")

    print(MENU_INSTRUCTIONS)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter Filename: ")
            load_or_save_projects(projects, filename, "load")
        elif choice == "S":
            filename = input("Enter Filename: ")
            load_or_save_projects(projects, filename, "save")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option.")
        print(MENU_INSTRUCTIONS)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_or_save_projects(projects, filename, action):
    """Load or save projects to a file based on the specified action."""
    if action == "load":
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
    elif action == "save":
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
    new_project = collect_project_details()
    if new_project:
        projects.append(new_project)


def collect_project_details():
    """Collect project details from user input."""
    project_name = input("Name: ")
    start_date = get_valid_input("Start date (dd/mm/yyyy): ", "date")
    priority = get_valid_input("Priority: ", "integer")
    cost_estimate = get_valid_input("Cost estimate: $", "float")
    percent_completion = get_valid_input("Percent complete: ", "integer")

    if start_date and priority is not None and cost_estimate is not None and percent_completion is not None:
        return Project(project_name, start_date, priority, cost_estimate, percent_completion)
    else:
        print("Invalid input.  Project details not collected.")
        return None


def get_valid_input(prompt, input_type):
    """Get a valid date input from the user based on the specified input type."""
    while True:
        try:
            if input_type == "date":
                date_string = input(prompt)
                try:
                    return datetime.strptime(date_string, "%d/%m/%Y").strftime("%d/%m/%Y")
                except ValueError:
                    print("Invalid date format.  Please use 'dd/mm/yyyy'.")
            elif input_type == "integer":
                return int(input(prompt))
            elif input_type == "float":
                return float(input(prompt))
            else:
                print("Invalid input type.")
        except ValueError:
            print(f"Invalid input.  Please enter a valid '{input_type}'.")


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


def filter_projects_by_date(projects):
    """Filter projects by date."""
    is_valid_input = False
    while not is_valid_input:
        project_start_date_string = input("Show projects that start after date (dd/mm/yy): ")
        project_start_date = datetime.strptime(project_start_date_string, "%d/%m/%Y")
        if project_start_date:  # This will check project_start_date is not equal to none
            is_valid_input = True

    sorted_projects = filter_and_sort_projects_by_date(projects, project_start_date)

    if sorted_projects:
        print(f"Filtered and sorted projects starting after {project_start_date.strftime('%d/%m/%Y')} are: ")
        for project in sorted_projects:
            print(project)


def filter_and_sort_projects_by_date(projects, start_date):
    """Filter and sort projects by start date."""
    if start_date:
        filtered_projects = [project for project in projects if
                             datetime.strptime(project.start_date, "%d/%m/%Y") > start_date]
        sorted_projects = sorted(filtered_projects, key=lambda x: datetime.strptime(x.start_date, "%d/%m/%Y"))
        return sorted_projects
    return []


main()
