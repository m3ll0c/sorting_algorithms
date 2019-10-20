"""
    Implementação batuta do Bubble Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm as Parent


class BubbleSort(Parent):

    def __init__(self, array):
        self.arr = array
        self.index = 0

    def next_iteration(self):
        if self.index < len(self.arr):
            self.iteration()
            self.index += 1
            return True
        return False

    def iteration(self):
        for j in range(0, len(self.arr) - 1):
            if self.arr[j] > self.arr[j + 1]:
                temp = self.arr[j + 1]
                self.arr[j + 1] = self.arr[j]
                self.arr[j] = temp

    def sort(self):
        while self.next_iteration():
            pass
