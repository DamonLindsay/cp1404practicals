"""
Wimbledon - Prac 05
Estimated: 40 minutes
Actual: 60+ Minutes
"""
FILENAME = "wimbledon.csv"


def main():
    """This program will read a file, process the data and display the processed information."""

    wimbledon_data = read_data(FILENAME)
    wimbledon_champion_to_win_count, countries_that_won_wimbledon = process_data(wimbledon_data)
    display_results(wimbledon_champion_to_win_count, countries_that_won_wimbledon)


def read_data(filename):
    """Read the data from a file, skipping the first line and returning relevant data."""
    wimbledon_data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for row in in_file:
            row = row.strip().split(",")
            wimbledon_data.append(row)
    return wimbledon_data


def process_data(data):
    """Process the data to calculate the champion win counts and list of countries."""
    wimbledon_champion_to_win_count = {}
    countries_that_won_wimbledon = set()

    for row in data:
        country_of_champion = row[1]
        countries_that_won_wimbledon.add(country_of_champion)

        champion = row[2]
        wimbledon_champion_to_win_count[champion] = wimbledon_champion_to_win_count.get(champion, 0) + 1
    return wimbledon_champion_to_win_count, countries_that_won_wimbledon


def display_results(champion_counts, countries):
    """Display the champion win counts and the list of countries that won."""
    print(f"Wimbledon Champions:")
    max_char_length_champions = max(len(champion) for champion in champion_counts)
    for wimbledon_champion, win_count in champion_counts.items():
        print(f"{wimbledon_champion:>{max_char_length_champions}} {win_count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
