"""Programming language classes with tests."""


class ProgrammingLanguage:

    def __int__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing},{self.reflection},{self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"


def run_tests():
    python = ProgrammingLanguage("Python", "Dynamic", True)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages = [python, ruby, visual_basic]
    print(python)
    print("The Dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
