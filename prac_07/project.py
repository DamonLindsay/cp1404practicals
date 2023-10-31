"""
Project class module
"""


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
        return (f"Name: {self.name}, Start Date: {self.start_date}, Priority: {self.priority}, "
                f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}")

    def __repr__(self):
        """Return the string representation of the Project object."""  # TODO BETTER DOCSTRING?
        return (f"Name: {self.name}, Start Date: {self.start_date}, Priority: {self.priority}, "
                f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}")
