"""Programming Language class module"""

class ProgrammingLanguage:
    """Programming Language class module"""
    def __init__(self, typing="", reflection=False, year=0):
        """Initialize the ProgrammingLanguage object."""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine whether the Typing is Dynamic (True) or not (False)."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

