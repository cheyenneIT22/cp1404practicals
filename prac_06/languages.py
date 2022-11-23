"""Programming language client input code."""
from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    print(python)
    print("The Dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
