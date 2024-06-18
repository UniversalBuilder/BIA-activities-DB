from database import Database
from project import Project

class UserInterface:
    def __init__(self, database):
        self.database = database

    def display_projects(self):
        projects = self.database.get_projects()
        for project in projects:
            print(project)

    def add_project(self):
        name = input("Enter project name: ")
        description = input("Enter project description: ")
        self.database.insert_project(Project(name, description))

    def update_project(self):
        id = input("Enter project id to update: ")
        name = input("Enter new project name: ")
        description = input("Enter new project description: ")
        self.database.update_project(Project(name, description, id))

    def delete_project(self):
        id = input("Enter project id to delete: ")
        self.database.delete_project(id)

    # Similar methods for files and logbook entries...
    
def main():
    database = Database('my_database.db')
    ui = UserInterface(database)

    while True:
        print("1. Display projects")
        print("2. Add project")
        print("3. Update project")
        print("4. Delete project")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ui.display_projects()
        elif choice == '2':
            ui.add_project()
        elif choice == '3':
            ui.update_project()
        elif choice == '4':
            ui.delete_project()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()