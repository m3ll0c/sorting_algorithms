"""
    Implementação batuta do Bogo Sort
"""

from algorithms.SortAlgorithm import SortAlgorithm
from random import randint


class BogoSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array
        self.index = 1

    def next_iteration(self):
        if not self.is_sorted():
            self.iteration()
            return False
        else:
            return True

    def iteration(self):
        for i in range(0, len(self.arr)):
            i = randint(0, len(self.arr) - 1)
            j = randint(0, len(self.arr) - 1)
            temp = self.arr[j]
            self.arr[j] = self.arr[i]
            self.arr[i] = temp

    def sort(self):
        while not self.next_iteration():
            pass

    def sort_lim(self, limit):
        while not self.next_iteration():
            self.index += 1
            if self.index >= limit:
                return
