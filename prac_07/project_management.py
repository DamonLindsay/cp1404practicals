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
    """This menu-based program will allow a user to manage project data based on user choices in the menu."""
    projects = []

    load_projects(projects, DEFAULT_FILENAME)

    print(MENU_INSTRUCTIONS)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter Filename: ")
            load_projects(projects, filename)
        elif choice == "S":
            filename = input("Enter Filename: ")
            save_projects(projects, filename)
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
    save_projects(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(projects, filename):
    """Load projects from a file."""
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


def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, "w", encoding="utf-8") as output_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=output_file)


def display_projects(projects):
    """Display all projects, sorted by priority.  Separates and displays incomplete and complete projects."""
    sorted_projects = projects
    sorted_projects.sort()
    print("Incomplete projects: ")
    display_project_status(sorted_projects, False)  # Display incomplete projects
    print("Completed projects: ")
    display_project_status(sorted_projects, True)  # Display completed projects


def display_project_status(projects, is_completed):
    """Display projects based on completion status, complete or incomplete."""
    if is_completed is False:
        for project in projects:
            if project.completion_percentage < 100:
                print(f"  {project}")
    else:
        for project in projects:
            if project.completion_percentage == 100:
                print(f"  {project}")


def add_project(projects):
    """Add a new project to the list after collecting and validating project details."""
    new_project = collect_project_details()
    if new_project:
        projects.append(new_project)


def collect_project_details():
    """Collect and validate project details from user input."""
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
    """Get a valid input from the user based on the specified input type."""
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
    """Update a chosen project with new completion percentage and priority based on user input."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    while True:
        try:
            project_choice = int(input("Project choice: "))
            if 0 <= project_choice < len(projects):
                print(projects[project_choice])

                new_percentage = input("New Completion Percentage: ")
                new_priority = input("New Priority: ")
                if new_percentage:
                    projects[project_choice].completion_percentage = int(new_percentage)
                if new_priority:
                    projects[project_choice].priority = int(new_priority)
                break
            else:
                print("Invalid project choice.  Please enter a valid index.")
        except ValueError:
            print("Invalid input.  Please enter a valid integer for project choice.")


def filter_projects_by_date(projects):
    """Filter and display projects that start after the specified date."""
    while True:
        project_start_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
        try:
            project_start_date = datetime.strptime(project_start_date_string, "%d/%m/%Y")
            filtered_projects = [project for project in projects if
                                 datetime.strptime(project.start_date, "%d/%m/%Y") > project_start_date]
            sorted_projects = sorted(filtered_projects, key=lambda x: datetime.strptime(x.start_date, "%d/%m/%Y"))

            if sorted_projects:
                print(f"Filtered and sorted projects starting after {project_start_date.strftime('%d/%m/%Y')} are: ")
                for project in sorted_projects:
                    print(project)
                break
            else:
                print("No projects found after the specified date.")
        except ValueError:
            print("Invalid date format.  Please use 'dd/mm/yyyy'.")


main()
