"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    """This program will take sales as input and then calculate your bonus amount."""
    sales = get_sales()
    while sales >= 0:
        bonus_amount = calculate_bonus(sales)
        print(f"Your bonus will be ${bonus_amount:.2f}.")
        sales = get_sales()


def calculate_bonus(sales):
    """Calculate the bonus based on sales."""
    if sales < 1000:
        bonus_amount = sales * 0.10
    else:
        bonus_amount = sales * 0.15
    return bonus_amount


def get_sales():
    """Take sales as an input."""
    sales = float(input("Enter sales: $"))
    return sales


main()
