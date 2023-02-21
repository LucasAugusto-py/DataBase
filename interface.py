from PySide6.QtWidgets import QWidget, QVBoxLayout
from classes import Table,NavBar, Formulary, Footer

class Main(QWidget):
    def __init__(self):
        super().__init__()
        header = NavBar()
        form = Formulary()
        table = Table("lavadero")
        footer = Footer()

        layout = QVBoxLayout()
        layout.addWidget(header)
        layout.addWidget(form)
        layout.addWidget(table)
        layout.addWidget(footer)

        self.setLayout(layout)