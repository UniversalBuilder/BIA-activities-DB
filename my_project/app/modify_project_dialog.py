from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ModifyProjectDialog(QDialog):
    def __init__(self, project):
        super().__init__()

        self.setWindowTitle("Modify Project")

        self.layout = QVBoxLayout(self)

        self.name_label = QLabel("Name")
        self.layout.addWidget(self.name_label)

        self.name_field = QLineEdit(project.name)
        self.layout.addWidget(self.name_field)

        self.description_label = QLabel("Description")
        self.layout.addWidget(self.description_label)

        self.description_field = QLineEdit(project.description)
        self.layout.addWidget(self.description_field)

        self.save_button = QPushButton("Save")
        self.layout.addWidget(self.save_button)

        # TODO: Connect the "Save" button to a function that saves the changes