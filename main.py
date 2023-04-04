from PySide6.QtWidgets import QApplication
from src.genetic import genetic_algorithm
from src.beam import beam_search

opt = -1
while opt != 0:
    print("\nQual algoritmo deseja executar?\n1 - Algoritmo Genético\n2 - Algoritmo de Busca em Feixe\n0 - Sair")
    try:
        opt = int(input())
    except ValueError:
        print("\nFavor digitar um número")
        continue
    if(opt == 1):
        genetic_algorithm()
    elif(opt == 2):
        beam_search()
    elif(opt == 0):
        print("\nFinalizado!")
    else:
        print("\nOpção inválida")
        