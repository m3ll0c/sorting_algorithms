"""
    Implementação marota do Pancake Sort
    Author: Victtor Mendes
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time


class PancakeSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array
        self.lastPancake = len(array) - 1

    def flip(self, i):
        start = 0
        while start < i:
            self.arr[start], self.arr[i] = self.arr[i], self.arr[start]
            start += 1
            i -= 1
            time.sleep(.5)

    def find_max_index(self, last_pancake):
        bigger_index = 0
        for i in range(0, last_pancake + 1):
            if self.arr[i] > self.arr[bigger_index]:
                bigger_index = i
            time.sleep(.5)
        return bigger_index

    def sort(self):
        for last_pancake in reversed(range(1, len(self.arr))):
            # gets the maximum index value in the array
            bigger_index = self.find_max_index(last_pancake)
            # flips the bigger number to the start of the array
            self.flip(bigger_index)
            # flips the bigger number to the last non-fixed position
            self.flip(last_pancake)
