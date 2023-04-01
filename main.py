from PySide6.QtWidgets import QApplication
from genetic import genetic_algorithm
from beam import beam_search
sum=0
itr=10
for i in range(itr):
    # sum += genetic_algorithm()
    sum += beam_search()

print("MEAN", sum/itr)
