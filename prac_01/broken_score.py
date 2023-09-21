"""
CP1404/CP5632 - Practical
Broken program to determine score status

The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""


def main():
    """This program gets the score via input, and then calculates the appropriate message for that score."""
    score = get_score()

    if score < 0 or score > 100:
        print("Invalid score.")
    elif score >= 90:
        print("Excellent.")
    elif score >= 50:
        print("Pass.")
    else:
        print("Bad.")


def get_score():
    """Get the score via input and then return it."""
    score = float(input("Enter score: "))
    return score


main()
