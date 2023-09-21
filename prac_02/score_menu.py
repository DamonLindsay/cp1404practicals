"""
Score Menu
"""

MENU_OPTIONS = ("(G)et a valid score\n"
                "(P)rint result\n"
                "(S)how stars\n"
                "(Q)uit")


def main():
    """This is a menu-based program that interacts with the user's score in various ways."""
    score = 0

    print(MENU_OPTIONS)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result_message = determine_result_message(score)
            print(result_message)
        elif choice == "S":
            if score <= 0:
                print("No stars to show :(")
            else:
                print_stars_score(score)
                print()
        else:
            print("Invalid input.")
        print(MENU_OPTIONS)
        choice = input(">>> ").upper()
    print("Farewell.")


def print_stars_score(score):
    """Prints a number of stars based on the given score."""
    for i in range(score):
        print("*", end="")


def get_valid_score():
    """Prompt the user for a valid score."""
    score = int(input("Please enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Please enter a score (0-100): "))
    return score


def determine_result_message(score):
    """Determine the appropriate message based on the given score."""
    if score < 0 or score > 100:
        score_message = "Invalid score."
        return score_message
    if score >= 90:
        score_message = "Excellent."
        return score_message
    if score >= 50:
        score_message = "Pass."
        return score_message
    score_message = "Bad."
    return score_message


main()
