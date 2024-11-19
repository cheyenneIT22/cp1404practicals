"""CP1404-Practical 07,
Project Management program
Estimated time to complete: 1 hour began at 5:50pm
Actual completed time: less than half an hour finished at 6:22pm."""
from datetime import datetime

from prac_07.project import Project


def main():
    projects = load_projects()
    menu = """
    Menu:
    (L)oad projects
    (S)ave projects
    (D)isplay projects
    (F)ilter projects by date
    (A)dd new project
    (U)pdate project
    (Q)uit
    """
    print(menu)
    choice = input("Choose an option: ")
    if choice == 'L':
        filename = input("Enter filename to load projects: ")
        load_projects(filename)
    elif choice == 'S':
        filename = input("Enter filename to save projects: ")
        save_projects(projects, filename)
    elif choice == 'D':
        display_projects(projects)
    elif choice == 'F':
        date = input("Enter date (YYYY-MM-DD) to filter projects: ")
        filter_projects_by_date(projects, date)
    elif choice == 'A':
        projects.append(add_new_project())
    elif choice == 'U':
        update_project(projects)
    elif choice == 'Q':
        save_choice = input("Would you like to save changes? (y/n): ").lower()
        if save_choice == 'y':
            save_projects(projects)
        print("Goodbye!")
    else:
        print("Invalid choice, please try again.")


def load_projects(filename="projects.txt"):
    projects = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, start_date, priority, completion = line.strip().split(',')
                projects.append(Project(name, start_date, priority, completion))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return projects


def save_projects(projects, filename="projects.txt"):
    with open(filename, 'w') as file:
        for project in projects:
            file.write(
                f"{project.name},{project.start_date.strftime('%Y-%m-%d')},{project.priority},{project.completion}\n")


def display_projects(projects):
    print("\nIncomplete Projects:")
    for project in sorted([p for p in projects if not p.is_completed()], key=lambda p: p.priority):
        print(project)
    print("\nCompleted Projects:")
    for project in sorted([p for p in projects if p.is_completed()], key=lambda p: p.priority):
        print(project)


def filter_projects_by_date(projects, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    filtered_projects = [p for p in projects if p.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project():
    name = input("Enter project name: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    priority = input("Enter priority (lower is higher): ")
    completion = input("Enter completion percentage: ")
    return Project(name, start_date, priority, completion)


def update_project(projects):
    display_projects(projects)
    try:
        project_index = int(input("Enter the number of the project to update: ")) - 1
        project = projects[project_index]
        new_completion = input(f"Enter new completion % (current: {project.completion}): ") or project.completion
        new_priority = input(f"Enter new priority (current: {project.priority}): ") or project.priority
        project.completion = int(new_completion)
        project.priority = int(new_priority)
    except (IndexError, ValueError):
        print("Invalid project selection.")


if __name__ == "__main__":
    main()
