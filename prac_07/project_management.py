"""CP1404-Practical 07,
Project Management program
Estimated time to complete: 1 hour
actual completed time: """
from prac_07.project import Project


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


def main():
    projects = load_projects()
    menu = """
    Menu:
    (L)oad projects
    (S)ave projects
    (D)isplay projects
    (F)ilter projects by date
    Add new project
    Update project
    Quit
    """
    print(menu)
    choice = input("Choose an option: ")
    if choice == 'L':
        filename = input("Enter filename to load projects: ")
        projects = load_projects(filename)
    elif choice == 'S':
        filename = input("Enter filename to save projects: ")
        save_projects(projects, filename)

        elif choice == '3':
            display_projects(projects)

        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD) to filter projects: ")
            filter_projects_by_date(projects, date)

        elif choice == '5':
            projects.append(add_new_project())

        elif choice == '6':
            update_project(projects)

        elif choice == '7':
            save_choice = input("Would you like to save changes? (y/n): ").lower()
            if save_choice == 'y':
                save_projects(projects)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

