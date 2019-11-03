"""
    Implementação Batuta do Counting Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time

class CountingSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    # contém a implementação da lógica da ordenação
    def sort(self):
        greater = None
        for i in range(0, len(self.arr)):
            if i < 1:
                greater = self.arr[i]
            if self.arr[i] > greater:
                greater = self.arr[i]

        aux = [0] * (greater + 1)

        for e in self.arr:
            aux[e] += 1

        index = 0
        size = len(self.arr)
        for i in range(0, len(aux)):
            dump = [i] * aux[i]
            time.sleep(0.5)
            for e in dump:
                index += 1
                self.arr.insert(index-1, e)
            self.arr = self.arr[:size]
