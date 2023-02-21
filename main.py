from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import Qt
from interface import Main
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.openDB()
        self.interface()
    
    def openDB(self):
        db = QSqlDatabase().addDatabase('QSQLITE')
        db.setDatabaseName('DataBase.db')
        if not db.open():
            print("No se puede inciar la base de datos")
        query = QSqlQuery()
        query.exec(f"""
        CREATE TABLE lavadero(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        patent VARCHAR(30),
        hour TIME,
        name VARCHAR(30),
        car VARCHAR(30),
        phone VARCHAR(30),
        note VARCHAR(255),
        price INTEGER
        )
        """)
    def interface(self):
        main = Main()
        self.setCentralWidget(main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

