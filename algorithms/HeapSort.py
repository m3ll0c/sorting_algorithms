"""
    Implementação Batutua do HeapSort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm


class HeapSort(SortAlgorithm):

    def __init__(self, array):
        self.arr = array
        self.index = (len(self.arr) -1)

    def next_iteration(self):
        self.iteration()
        if self.index >= 0:
            self.arr[self.index], self.arr[0] = self.arr[0], self.arr[self.index]  # swap da massa
            self.heapify(self.arr, self.index, 0)
            self.index -= 1
            return True
        return False

    def iteration(self):
        for i in range(self.index, -1, -1):
            self.heapify(self.arr, self.index, i)

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

    def sort(self):
        while self.next_iteration():
            pass
