"""
Silver Service Taxi Test Module
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)

print(test_taxi)
print(f"Expected: 4.50, Actual: {test_taxi.get_fare():.2f}")

test_taxi.drive(18)
print(test_taxi)
print(F"Expected: 48.80, Actual: {test_taxi.get_fare():.2f}")
