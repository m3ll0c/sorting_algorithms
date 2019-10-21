"""
    Implementação batuta do Insertion Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm


class InsertionSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array
        self.index = 1  # 1 até tam(arr)

    def next_iteration(self):
        if self.index < len(self.arr):
            self.iteration()
            self.index += 1
            return True
        return False

    def iteration(self):
        j = self.index - 1
        key = self.arr[self.index]
        while j >= 0 and key < self.arr[j]:
            self.arr[j + 1] = self.arr[j]
            j -= 1
        self.arr[j + 1] = key

    def sort(self):
        while self.next_iteration():
            pass