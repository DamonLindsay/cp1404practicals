"""
Electricity Bill
"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    """This program will get the tariff, the daily kWh and billing days via input,
    and then calculate the total."""
    print("Electricity bill estimator 2.0")

    tariff_choice = input("Which tariff? 11 or 31: ")

    daily_use_in_kwh = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))

    price_per_kwh_in_cents = calculate_tariff_rate(tariff_choice)

    daily_kwh_use_in_dollars = price_per_kwh_in_cents * daily_use_in_kwh
    total_cost = daily_kwh_use_in_dollars * number_of_billing_days

    print(f"Estimated bill: ${total_cost:.2f}")


def calculate_tariff_rate(tariff_choice):
    """Decide which tariff is the correct rate based on user input."""
    if tariff_choice == "11":
        price_per_kwh_in_cents = TARIFF_11
    else:
        price_per_kwh_in_cents = TARIFF_31
    return price_per_kwh_in_cents


main()
