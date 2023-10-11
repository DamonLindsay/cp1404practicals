"""
Wimbledon - Prac 05
Estimated: 40 minutes
Actual: x Minutes
"""
FILENAME = "wimbledon.csv"


def main():
    """This program will read a file, process the data and display the processed information."""

    wimbledon_data = read_wimbledon_data(FILENAME)
    wimbledon_champion_to_win_count, countries_that_won_wimbledon = process_wimbledon_data(wimbledon_data)
    display_wimbledon_results(wimbledon_champion_to_win_count, countries_that_won_wimbledon)


def read_wimbledon_data(filename):
    """Read the Wimbledon data from a file, skipping the first line and returning relevant data."""
    wimbledon_data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for row in in_file:
            row = row.strip().split(",")
            wimbledon_data.append(row)
    return wimbledon_data


def process_wimbledon_data(data):
    """Process the Wimbledon data to calculate the champion win counts and list of countries."""
    wimbledon_champion_to_win_count = {}
    countries_that_won_wimbledon = set()

    for row in data:
        country_of_champion = row[1]
        countries_that_won_wimbledon.add(country_of_champion)

        champion = row[2]
        wimbledon_champion_to_win_count[champion] = wimbledon_champion_to_win_count.get(champion, 0) + 1
    return wimbledon_champion_to_win_count, countries_that_won_wimbledon


def display_wimbledon_results(champion_counts, countries):
    """Display the Wimbledon champion win counts and the list of countries that won."""
    print(f"Wimbledon Champions:")
    for wimbledon_champion, win_count in champion_counts.items():
        print(f"{wimbledon_champion} {win_count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
