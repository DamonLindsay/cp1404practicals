"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    """This program will display a dictionary of state codes and their corresponding state names, then prompts the
     to enter a state code, and displays the corresponding state name."""
    print(CODE_TO_NAME)

    max_char_length = calculate_max_char_length(CODE_TO_NAME)
    display_states(CODE_TO_NAME, max_char_length)

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(state_code, "is", CODE_TO_NAME[state_code])
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()


def calculate_max_char_length(code_to_name):
    """Calculate the maximum character length of state codes in the dictionary."""
    max_code_character_length = max(len(code) for code in code_to_name)
    return max_code_character_length


def display_states(code_to_name, max_code_character_length):
    """Display the state codes and names neatly formatted."""
    for code, name in code_to_name.items():
        print(f"{code:<{max_code_character_length}} is {name}")


main()
