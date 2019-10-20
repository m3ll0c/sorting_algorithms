"""
    Implementação Batuta do Counting Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm


class CountingSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    # executa uma iteração
    def next_iteration(self):
        if self.is_sorted() or len(self.arr) < 1:
            return False
        self.iteration()
        return True

    # contém a implementação da lógica da ordenação
    def iteration(self):
        greater = None
        temp = []
        for i in range(0, len(self.arr)):
            if i < 1:
                greater = self.arr[i]
            if self.arr[i] > greater:
                greater = self.arr[i]

        aux = [0] * (greater + 1)

        for e in self.arr:
            aux[e] += 1

        for i in range(0, len(aux)):
            dump = [i] * aux[i]
            temp.extend(dump)

        self.arr = temp

    # retorna o dataset
    def sort(self):
        self.next_iteration()