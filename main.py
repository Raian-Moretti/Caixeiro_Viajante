from PySide6.QtWidgets import QApplication
from genetic import genetic_algorithm
from beam import beam_search

for i in range(5):
    genetic_algorithm()
    beam_search()
