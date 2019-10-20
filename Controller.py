"""
    Classe que controla a execução dos algoritmos de ordenação
    Author: Gabriel Melo
"""

import time, traceback
from threading import Thread

class Controller:

    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.currentDatasets = {}  # armazena os conjuntos provenientes de cada algoritmo de ordenação

    """
        Retorna os dados provenientes das iterações dentro de um dicionário indexado pelo nome do algoritmo
    """
    def iter_all(self):
        datasets = {}
        for a in self.algorithms:
            a.next_iteration()
            datasets[type(a).__name__] = a.arr
        self.currentDatasets = datasets

    """
        Retorna os dados provenientes da ordenação dentro de um dicionário indexado pelo nome do algoritmo
    """
    def order_all(self):
        datasets = {}
        for a in self.algorithms:
            a.order()
            datasets[type(a).__name__] = a.arr
        self.currentDatasets = datasets