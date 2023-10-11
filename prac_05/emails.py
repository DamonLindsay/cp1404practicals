"""
Emails - Prac 05
Estimated: 20 minutes
Actual: 25 Minutes
"""


def main():
    """This program will store users' emails and names in a dictionary.  Once all the emails are stored, the program
    will loop through the dictionary and print them out."""

    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = email.split("@")[0]
        cleaned_name = clean_name(name)
        response = input(f"Is your name {cleaned_name}? (Y/n) ")

        if response.lower() in ("y", "yes", ""):
            email_to_name[email] = cleaned_name
        else:
            custom_name = input("Name: ")
            email_to_name[email] = custom_name
        email = input("Email: ")

    print_emails_and_names(email_to_name)


def clean_name(name):
    """Clean the name, removing periods and digits and then capitalizing it."""
    cleaned_name = ' '.join(character for character in name.split(".") if not character.isdigit()).title()
    return cleaned_name


def print_emails_and_names(email_to_name):
    """Print the email addresses and names."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
