"""
    Implementação batuta do Bogo Sort
"""

from algorithms.SortAlgorithm import SortAlgorithm
from random import randint
import time


class BogoSort(SortAlgorithm):

    def __init__(self, array, timeout):
        self.arr = array
        self.timeout = (timeout/1000) * 2

    def sort(self):
        while not self.is_sorted():
            time.sleep(self.timeout)
            for i in range(0, len(self.arr)):
                i = randint(0, len(self.arr) - 1)
                j = randint(0, len(self.arr) - 1)
                temp = self.arr[j]
                self.arr[j] = self.arr[i]
                self.arr[i] = temp