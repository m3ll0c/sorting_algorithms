"""
    Implementação Batutua do HeapSort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time


class HeapSort(SortAlgorithm):

    def __init__(self, array, timeout):
        self.arr = array
        self.size = len(self.arr)
        self.timeout = (timeout / 1000) * 2

    def sort(self):
        for i in range(self.size, -1, -1):
            self.heapify(self.arr, self.size, i)

        for i in range(self.size-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            time.sleep(self.timeout)
            self.heapify(self.arr, i, 0)
            time.sleep(self.timeout)

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap da massa
            self.heapify(arr, n, largest)