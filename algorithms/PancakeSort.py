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

    def flip(self, n):
        self.arr[:n + 1] = reversed(self.arr[:n + 1])

    def next_iteration(self):
        biggerIndex = self.arr.index(max(self.arr[:self.lastPancake + 1]))
        #flips the bigger number to the start of the array
        self.flip(biggerIndex)
        #flips the bigger number to the last non-fixed position
        self.flip(self.lastPancake)

    def iteration(self):
        pass

    def sort(self):
        for _ in range(len(self.arr) - 1):
            time.sleep(15/1000)
            self.next_iteration()
            self.lastPancake -= 1
