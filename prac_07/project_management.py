"""Project Management Program."""
import datetime

MENU = "- (L)oad Projects" \
       "- (S)ave projects" \
       "- (F)ilter projects by date" \
       "- (A)dd new project" \
       "- (U)pdate project" \
       "- (D)isplay projects" \
       "- (Q)uit"
FILENAME = "projects.txt"
PROJECT = """Name start date priority project"""


def main():
    projects = load_projects(FILENAME)
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            FILENAME = input("File to load: ")
            projects = load_projects(FILENAME)
        elif choice == "S":
            FILENAME = input("File to save:  ")
            save_projects(projects, FILENAME)
        elif choice == "A":
            add(projects)
        elif choice == "F":
            filter_project(datetime)
        elif choice == "U":
            update(projects)
        elif choice == "D":
            display(projects)
        else:
            print("Invalid project")
        choice = input(">>> ").upper()


def load_projects(FILENAME):
    projects = []
    with open(FILENAME, encoding="utf-8"):
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('Y')
            start_date = datetime.datetime
            project = project(parts[0], load_projects())
            return projects


def save_projects(projects, FILENAME):
    with open(FILENAME, "w", encoding="utf-8"):
        print(PROJECT, file=out_file)
        for project in projects:
            print(f"{project.name}\t{projects}"
                  f"{project.cost_estimate}")


def filter_project(datetime):
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))


def add(projects):
    index = int(input("Project choice:  "))
    start_date = int(input("Start date (dd/mm/yy): "))
    priority = int(input("Priority:"))
    cost_estimate = int(input("Cost estimate: "))
    percent_complete = int(input("Percent complete:  "))
    return projects


def update(projects):
    for i, project in enumerate(projects):
        print(i, project)
    new_percentage = int(input("New percentage: "))
    new_priority = int(input("New Priority:  "))
    return update


def display(projects):
    print("Incomplete projects:  ")
    incomplete_projects = [project for project in projects if project]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", projects)
    print("Completed projects: ")
    complete_projects = [project for project in projects if project]
    complete_projects.sort()
    for project in complete_projects:
        print("", project)
    complete_projects[0].name = "blah"
    print(id(complete_projects[0]))

    main()
