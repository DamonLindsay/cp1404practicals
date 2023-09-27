"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
1a. The ValueError will occur when a non-integer is entered into the numerator or denominator inputs.

2. When will a ZeroDivisionError occur?
2a. This error will occur when the fraction calculation occurs, if the denominator = 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
3a. Yes, you can add a condition that checks if the denominator = 0 before the calculation is attempted.
If the denominator = 0, display an error message and then ask the user to enter a valid number.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
