"""
Wimbledon - Prac 05
Estimated: 40 minutes
Actual: x Minutes
"""
FILENAME = "wimbledon.csv"


def main():
    """This program will read a file, process the data and display the processed information."""
    wimbledon_champion_to_win_count = {}
    countries_that_won_wimbledon = set()

    wimbledon_data = read_wimbledon_data(FILENAME)

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for row in in_file:
            row = row.split(",")
            country_of_champion = row[1]
            countries_that_won_wimbledon.add(country_of_champion)
            champion = row[2]
            try:
                wimbledon_champion_to_win_count[champion] += 1
            except KeyError:
                wimbledon_champion_to_win_count[champion] = 1

    print("Wimbledon Champions:")
    for wimbledon_champion, win_count in wimbledon_champion_to_win_count.items():
        print(f"{wimbledon_champion} {win_count}")
    print()
    print(f"These {len(countries_that_won_wimbledon)} countries have won Wimbledon: ")
    print(", ".join(list(sorted(countries_that_won_wimbledon))))


def read_wimbledon_data(filename):
    """Read the Wimbledon data from a file, skipping the first line and returning relevant data."""
    wimbledon_data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for row in in_file:
            row = row.strip().split(",")
            wimbledon_data.append(row)
    return wimbledon_data


main()
