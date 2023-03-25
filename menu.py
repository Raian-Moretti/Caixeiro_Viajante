from PySide6.QtWidgets import QVBoxLayout, QPushButton, QDialog
from beam import Beam
from genetic import Genetic

class Menu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose an option:")
        self.opt_1 = Beam
        self.opt_2 = Genetic
        self.resize(400,200)
        layout = QVBoxLayout()
        button1 = QPushButton("Beam Search")
        button1.clicked.connect(self.opt_1.beam_search)
        layout.addWidget(button1)
        button2 = QPushButton("Genetic Algorithm")
        button2.clicked.connect(self.opt_2.genetic_algorithm)
        layout.addWidget(button2)
        self.setLayout(layout)
