"""
Files - Prac 03
"""
NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"


def question_01():
    """Answer for question 1 for files.py."""
    name = input("Name: ")

    with open(NAME_FILE, "w") as out_file:
        print(f"{name}", file=out_file)


def question_02():
    """Answer for question 2 for files.py."""
    with open(NAME_FILE, "r") as in_file:
        name = in_file.read().strip()
        print(f"Your name is {name}.")


def question_03():
    """Answer for question 3 for files.py"""
    with open(NUMBERS_FILE, "r") as in_file:
        first_number = int(in_file.readline().strip())
        second_number = int(in_file.readline().strip())
        total = first_number + second_number
        print(total)


def question_04():
    """Answer for question 4 in files.py."""
    total = 0
    with open(NUMBERS_FILE, "r") as in_file:
        for line in in_file:
            number = int(line.strip())
            total += number
        print(total)


question_01()
question_02()
question_03()
question_04()
