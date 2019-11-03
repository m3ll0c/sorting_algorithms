"""
    Implementação Batuta do QuickSort
    Author: Gabriel Melo
"""
from algorithms.SortAlgorithm import SortAlgorithm
import time

class QuickSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array

    def sort(self):
        self.quickSort(self.arr, 0, len(self.arr)-1)

    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quickSort(self, arr, low, high):
        if low < high:
            time.sleep(0.5)
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)