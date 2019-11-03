"""
    Implementação Batuta do QuickSort
    Author: Gabriel Melo
"""
from algorithms.SortAlgorithm import SortAlgorithm
import time

class QuickSort(SortAlgorithm):

    def __init__(self, array, timeout):
        self.arr = array
        self.timeout = (timeout / 1000) * 2

    def sort(self):
        self.quick_sort(self.arr, 0, len(self.arr) - 1)

    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                time.sleep(self.timeout)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)
