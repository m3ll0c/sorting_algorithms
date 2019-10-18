"""
    Implementação batuta do Bogo Sort
"""

from algorithms.SortAlgorithm import SortAlgorithm as Parent
from random import randint

class BogoSort(Parent):

    def __init__(self, array):
        self.arr = array
        self.index = 1

    def next_iteration(self):
        if not self.isSorted():
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

    def sort(self, limit):
        while not self.next_iteration():
            self.index += 1
            if self.index >= limit:
                return

    def isSorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True
