"""
    Implementação batuta do Insertion Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time


class InsertionSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    def sort(self):
        for i in range(1, len(self.arr)):
            j = i - 1
            key = self.arr[i]
            while j >= 0 and key < self.arr[j]:
                time.sleep(0.5)
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
