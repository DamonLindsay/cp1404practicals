"""
More Scores - Practice / Extension
"""


def main():
    """This program will ask the user for a random number of scores, then generate that many random numbers.
    For each of those scores, write the result to a file."""
    pass


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
