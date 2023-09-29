"""
More Random Conrad - Extension
"""
import random

random_maximum_increase = random.uniform(0.075, 0.175)  # Random float between 7.5% and 17.5%
random_maximum_decrease = random.uniform(0.01, 0.05)  # Random float between 1% and 5%
random_minimum_price = random.uniform(0.01, 1.00)
random_maximum_price = random.uniform(50.00, 100.00)
random_initial_price = random.uniform(10.00, 50.00)
OUTPUT_FILE = "capitalist_conrad_output_file.txt"

out_file = open(OUTPUT_FILE, "w")

price = random_initial_price
print(f"Starting price: ${price:,.2f}", file=out_file)
number_of_days = 0

while random_minimum_price <= price <= random_maximum_price:
    price_change = 0
    number_of_days += 1

    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, random_maximum_increase)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-random_maximum_decrease, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
