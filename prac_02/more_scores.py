"""
More Scores - Practice / Extension
"""
import random


def main():
    """This program will ask the user for a random number of scores, then generate that many random numbers.
    For each of those scores, write the result to a file."""
    number_of_scores = int(input("Enter a number of random scores to generate: "))

    for score in range(number_of_scores):
        score = random.randint(0, 100)
        print(f"{score} is {determine_result_message(score)}.")


def determine_result_message(score):
    """Determine the appropriate message based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()
