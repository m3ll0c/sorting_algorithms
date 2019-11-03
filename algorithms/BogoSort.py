"""
    Implementação batuta do Bogo Sort
"""

from algorithms.SortAlgorithm import SortAlgorithm
from random import randint
import time


class BogoSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    def sort(self):
        while not self.is_sorted():
            time.sleep(0.5)
            for i in range(0, len(self.arr)):
                i = randint(0, len(self.arr) - 1)
                j = randint(0, len(self.arr) - 1)
                temp = self.arr[j]
                self.arr[j] = self.arr[i]
                self.arr[i] = temp
