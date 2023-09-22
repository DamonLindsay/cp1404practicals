"""
Gopher Population Simulator - Extension
"""
import random


def main():
    """This program will simulate a secret population of gophers, where a random amount of
    births and deaths occur over a predetermined timespan."""
    total_years_to_simulate = 10
    gopher_population = 1000

    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {gopher_population}")
    print(f"Year 1")
    print()

    for year in range(2, total_years_to_simulate + 1):
        gopher_population = simulate_year(gopher_population)
        print(f"Population: {gopher_population}")
        print(f"Year {year}")
        print()


def simulate_year(gopher_population):
    """Simulate one year of gopher population."""
    new_births = calculate_new_births(gopher_population)
    gopher_population += new_births

    new_deaths = calculate_new_deaths(gopher_population)
    gopher_population -= new_deaths

    print(f"{new_births} gophers were born.  {new_deaths} died.")
    return int(gopher_population)


def calculate_new_births(population):
    """Calculate the number of new births based on the population."""
    return int(population * random.uniform(0.10, 0.20))


def calculate_new_deaths(population):
    """Calculate the number of new deaths based on the population."""
    return int(population * random.uniform(0.05, 0.25))


main()
