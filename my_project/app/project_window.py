from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

class ProjectWindow(QMainWindow):
    def __init__(self, project):
        super().__init__()

        self.setWindowTitle(project.name)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.new_file_button = QPushButton("New File")
        self.layout.addWidget(self.new_file_button)

        self.new_logbook_entry_button = QPushButton("New Logbook Entry")
        self.layout.addWidget(self.new_logbook_entry_button)

        # TODO: Add widgets to display the project files and logbook entries