from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFrame, QSizePolicy, QDialog, QLineEdit, QLabel, QDialogButtonBox
from project import Project

class NewProjectDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Project")

        self.layout = QVBoxLayout(self)

        self.name_label = QLabel("Name:")
        self.layout.addWidget(self.name_label)

        self.name_edit = QLineEdit()
        self.layout.addWidget(self.name_edit)

        self.description_label = QLabel("Description:")
        self.layout.addWidget(self.description_label)

        self.description_edit = QLineEdit()
        self.layout.addWidget(self.description_edit)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def get_details(self):
        return self.name_edit.text(), self.description_edit.text()

class MainWindow(QMainWindow):
    def __init__(self, database):
        super().__init__()

        self.database = database

        self.setWindowTitle("Project Tracker")
        self.setGeometry(0, 0, 1024, 678)  # Set window size to 1024x678

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QHBoxLayout(self.main_widget)  # Use QHBoxLayout for main layout

        # Create a sidebar
        self.sidebar = QFrame()
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)

        self.sidebar_layout = QVBoxLayout(self.sidebar)  # Use QVBoxLayout for sidebar layout

        self.new_project_button = QPushButton("New Project")
        self.new_project_button.clicked.connect(self.open_new_project_dialog)
        self.sidebar_layout.addWidget(self.new_project_button)

        # TODO: Add more widgets to the sidebar

        self.layout.addWidget(self.sidebar)
        
        # Add a stretchable space to the right of the sidebar
        self.layout.addStretch(1)

        # TODO: Add more widgets to the main layout
        
    def open_new_project_dialog(self):
        dialog = NewProjectDialog()
        result = dialog.exec()

        if result == QDialog.Accepted:
            name, description = dialog.get_details()
            self.create_new_project(name, description)

    def create_new_project(self, name, description):
        # Create a new project instance
        project = Project(name, description)
        
        # Add the project to the database
        self.database.add_project(project)
        
        # Update the UI to reflect the new project
        self.update_ui()
        
    def update_ui(self):
        # TODO: Update the UI to reflect changes in the database
        pass