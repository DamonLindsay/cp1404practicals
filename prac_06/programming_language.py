"""Programming Language class module"""


class ProgrammingLanguage:
    """Programming Language class module"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize the ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return the string version of the ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine whether the Typing is Dynamic (True) or not (False)."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
