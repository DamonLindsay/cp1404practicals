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


def question_03():
    """Answer for question 3 for files.py"""
    with open("numbers.txt", "r") as in_file:
        first_number = int(in_file.readline().strip())
        second_number = int(in_file.readline().strip())
        total = first_number + second_number
        print(total)


# question_01()
# question_02()
question_03()
