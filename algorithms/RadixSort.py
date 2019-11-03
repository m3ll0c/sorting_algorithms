"""
    Implementação batuta do Radix Sort
    Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm
import time, math


class RadixSort(SortAlgorithm):
    
    def __init__(self, array, timeout):
        self.arr = array
        self.timeout = (timeout / 1000) * 2

    def counting_sort(self, arr, exp1):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)
        for i in range(0, n):
            index = (arr[i] / exp1)
            count[math.floor((index) % 10)] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            time.sleep(self.timeout)
            index = (arr[i] / exp1)
            output[count[math.floor((index) % 10)] - 1] = arr[i]
            count[math.floor((index) % 10)] -= 1
            i -= 1
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def sort(self):
        max1 = max(self.arr)
        exp = 1

        while max1 / exp > 0:
            self.counting_sort(self.arr, exp)
            exp *= 10
