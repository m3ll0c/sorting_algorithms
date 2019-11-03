"""
    Implementação batuta do Bubble Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time

class BubbleSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    def sort(self):
        for i in range(0, len(self.arr)):
            for j in range(0, len(self.arr) - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    time.sleep(0.5)
                    temp = self.arr[j + 1]
                    self.arr[j + 1] = self.arr[j]
                    self.arr[j] = temp