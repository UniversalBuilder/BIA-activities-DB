from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class NewLogbookEntryDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Logbook Entry")

        self.layout = QVBoxLayout(self)

        self.details_label = QLabel("Details")
        self.layout.addWidget(self.details_label)

        self.details_field = QLineEdit()
        self.layout.addWidget(self.details_field)

        self.create_button = QPushButton("Create")
        self.layout.addWidget(self.create_button)

        # TODO: Connect the "Create" button to a function that creates the logbook entry