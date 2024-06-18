from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class NewFileDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New File")

        self.layout = QVBoxLayout(self)

        self.name_label = QLabel("Name")
        self.layout.addWidget(self.name_label)

        self.name_field = QLineEdit()
        self.layout.addWidget(self.name_field)

        self.create_button = QPushButton("Create")
        self.layout.addWidget(self.create_button)

        # TODO: Connect the "Create" button to a function that creates the file