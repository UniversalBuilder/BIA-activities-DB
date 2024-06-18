from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from database import Database

def main():
    db = Database('./resources/database.db')
    app = QApplication([])
    window = MainWindow(db)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()