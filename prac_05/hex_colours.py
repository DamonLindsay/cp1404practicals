"""
Hex Colours - Prac 05

Based on the state name example program above, create a program that allows you to look up hexadecimal colour codes
like those at http://www.color-hex.com/color-names.html

Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get
the code, e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""

COLOUR_NAME_TO_COLOUR_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                              "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                              "Amethyst": "#9966cc", "Antique White": "#faebd7", "Apricot": "#fbceb1",
                              "Aqua": "#00ffff"}

