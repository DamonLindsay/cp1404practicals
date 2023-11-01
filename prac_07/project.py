"""
Project class module
"""
from datetime import datetime


class Project:
    """The Project class."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize the Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return the string representation of the Project object."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"Cost estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return the string representation of the Project object."""  # TODO BETTER DOCSTRING?
        return (f"Name: {self.name}, Start Date: {self.start_date}, Priority: {self.priority}, "
                f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}")

    def __lt__(self, other):
        """Determine which project is less important based on its priority."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Determine which project is equally import based on its priority."""
        return self.priority == other.priority

    def __gt__(self, other):
        """Determine which project is more important based on its priority."""
        return self.priority > other.priority
