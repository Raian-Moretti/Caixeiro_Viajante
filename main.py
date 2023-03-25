from PySide6.QtWidgets import QApplication
from menu import Menu

app = QApplication([])
menu = Menu()
menu.show()
app.exec_()
