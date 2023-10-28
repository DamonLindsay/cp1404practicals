"""
Expected Time: 30 mins (4:27pm start)
Actual Time:
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print()  # Separate initial part of program from 2nd half.

programming_languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
                         ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                         ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print("The dynamically typed languages are: ")
for programming_language in programming_languages:
    if programming_language.is_dynamic():
        print(programming_language.name)
