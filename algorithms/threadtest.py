from threading import Thread
import time

from algorithms.BogoSort import BogoSort
from algorithms.BubbleSort import BubbleSort
from algorithms.CountingSort import CountingSort
from algorithms.HeapSort import HeapSort
from algorithms.InsertionSort import InsertionSort
from algorithms.MergeSort import MergeSort
from algorithms.QuickSort import QuickSort
from algorithms.RadixSort import RadixSort


obj = QuickSort([5,3,5,2,1,1,0,9,12, 13, 11])

def sh():
    while True:
        print(str(len(obj.arr))+str(obj.arr))
        time.sleep(.50)

t = Thread(target=obj.sort)
t2 = Thread(target=sh)

t2.start()
t.start()