"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """This program will read subject data from a text file, and the print the subject information."""
    data = get_data()
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def print_subject_details(subjects):
    """Print the subject details"""
    maximum_subject_name_character_length = max(len(str(subject[0])) for subject in subjects)
    maximum_teacher_name_character_length = max(len(str(subject[1])) for subject in subjects)
    maximum_number_of_students_character_length = max(len(str(subject[2])) for subject in subjects)

    for subject in subjects:
        print(f"{subject[0]:>{maximum_subject_name_character_length}} is taught by "
              f"{subject[1]:>{maximum_teacher_name_character_length}} and "
              f"has {subject[2]:>{maximum_number_of_students_character_length}} students.")


main()
