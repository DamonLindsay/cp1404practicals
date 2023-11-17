"""
Silver Service Taxi Test Module
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)

print(hummer)
print(f"Expected: 4.50, Actual: {hummer.get_fare():.2f}")

hummer.drive(18)
print(hummer)
print(F"Expected: 48.80, Actual: {hummer.get_fare():.2f}")
