"""
    Implementação batuta do Merge Sort
"""

from algorithms.SortAlgorithm import SortAlgorithm as Parent
from math import floor


class MergeSort(Parent):

    def next_iteration(self):
        pass

    def iteration(self):
        pass

    def sort(self):
        pass










def merge(llist, rlist):
    final = []
    while llist or rlist:

        if len(llist) and len(rlist):
            if llist[0] < rlist[0]:
                final.append(llist.pop(0))
            else:
                final.append(rlist.pop(0))

        if not len(llist):
            if len(rlist): final.append(rlist.pop(0))

        if not len(rlist):
            if len(llist): final.append(llist.pop(0))

    return final


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = floor(len(arr)/2)

    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))



print(merge_sort([2,3,4,1,0,99,13]))