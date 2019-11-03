"""
    Implementação marota do SelectionSort
    Author: Victtor Mendes
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time


class SelectionSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    def find_min_index(self, start):
        min_index = start
        for j in range(start + 1, len(self.arr)):
            if self.arr[j] < self.arr[min_index]:
                min_index = j
            time.sleep(.5)
        return min_index

    def sort(self):
        for i in range(len(self.arr) - 1):
            # finds the smaller value in the array
            min_index = self.find_min_index(i)
            # puts the smaller value in the first non-fixed position
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            time.sleep(.5)
