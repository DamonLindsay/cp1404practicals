"""
CP1404/CP5632 - Practical
Broken program to determine score status

The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""
import random


def main():
    """This program will get a score via input, and then determine the
    appropriate message for that score.  It well then repeat with a random number between 1-100."""
    score = float(input("Enter score: "))

    result_message = determine_result_message(score)
    print(result_message)

    random_score = random.randint(1, 100)
    print(f"Random number generated was: {random_score}")

    result_message = determine_result_message(random_score)
    print(result_message)


def determine_result_message(score):
    """Determine the appropriate message based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Pass."
    return "Bad."


main()
