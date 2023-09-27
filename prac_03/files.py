"""
Files - Prac 03
"""
FILE = "name.txt"


def question_01():
    """Answer for question 1 for files.py."""
    name = input("Name: ")

    with open(FILE, "w") as out_file:
        print(f"{name}", file=out_file)


def question_02():
    """Answer for question 2 for files.py."""
    with open(FILE, "r") as in_file:
        name = in_file.readline().strip()
        print(f"Your name is {name}.")


# question_01()
question_02()
