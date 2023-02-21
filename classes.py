from PySide6.QtWidgets import QWidget, QTableView, QHeaderView, QAbstractItemView, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QLabel, QCheckBox
from PySide6.QtSql import QSqlTableModel


class NavBar(QWidget):
    def __init__(self):
        super().__init__()
        title_name = QLabel()
        nav_bar = QHBoxLayout()
        language = QCheckBox()
        dark_light = QCheckBox() 

class Formulary(QWidget):
    label = {
        "patent":"Patete",
        "name":"Nombre",
        "hour":"Hora",
        "car":"Vehiculo",
        "phone":"Celular",
        "note":"Observaciones"
    }
    qss = ""
    def __init__(self):
        super().__init__()

        self.label_patent = QLabel(self.label["patent"])
        self.label_hour = QLabel(self.label["hour"])
        self.label_name = QLabel(self.label["name"])
        self.label_car =  QLabel(self.label["car"])
        self.label_phone = QLabel(self.label["phone"])
        self.label_note = QLabel(self.label["note"])

        self.patent = QLineEdit()
        self.hour = QSpinBox()
        self.name = QLineEdit()
        self.car = QLineEdit()
        self.phone = QLineEdit()
        self.note = QLineEdit()

        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(self.label_patent)
        hLayout1.addWidget(self.patent)
        hLayout1.addWidget(self.label_hour)
        hLayout1.addWidget(self.hour)
        hLayout1.addWidget(self.label_name)
        hLayout1.addWidget(self.name)

        hLayout2 = QHBoxLayout()
        hLayout2.addWidget(self.label_car)
        hLayout2.addWidget(self.car)
        hLayout2.addWidget(self.label_phone)
        hLayout2.addWidget(self.phone)
        hLayout2.addWidget(self.label_note)
        hLayout2.addWidget(self.note)


        layout = QVBoxLayout()
        layout.addLayout(hLayout1)
        layout.addLayout(hLayout2)

        self.setStyleSheet(self.qss)
        self.setLayout(layout)

class Table(QWidget):
    def __init__(self, sql_table):
        super().__init__()
        self.table = QTableView()
        self.table.model = QSqlTableModel()
        self.table.model.setTable(sql_table)
        self.table.model.select()
        self.table.setModel(self.table.model)
        self.table.resizeColumnsToContents()
        self.table.setColumnHidden(0, True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

class Footer(QWidget):
    name = "LucasAugusto.py"
    page = "LucasAugusto.com"
    email = "lucasaugusto@gmail.com"
    def __init__(self):
        super().__init__()
        name = QLabel(self.name)
        page = QLabel(self.page)
        email = QLabel(self.email)

        layout = QHBoxLayout()
        layout.addWidget(name)
        layout.addWidget(page)
        layout.addWidget(email)

        self.setLayout(layout)
        


