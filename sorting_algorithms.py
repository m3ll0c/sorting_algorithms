"""
" Ponto de entrada do programa
" Author: Gabriel Melo
"""
from intro import intros
from algorithms.MergeSort import MergeSort
from algorithms.QuickSort import QuickSort
from algorithms.RadixSort import RadixSort
from algorithms.InsertionSort import InsertionSort
from algorithms.CountingSort import CountingSort
from algorithms.BubbleSort import BubbleSort
from algorithms.BogoSort import BogoSort
from algorithms.HeapSort import HeapSort
from algorithms.PancakeSort import PancakeSort
from random import randint
import argparse, time
from threading import Thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init_algs(dataset):
    algs = list()
    algs.append(InsertionSort(dataset.copy()))
    algs.append(BubbleSort(dataset.copy()))
    algs.append(BogoSort(dataset.copy()))
    algs.append(CountingSort(dataset.copy()))
    algs.append(HeapSort(dataset.copy()))
    algs.append(MergeSort(dataset.copy()))
    algs.append(PancakeSort(dataset.copy()))
    algs.append(QuickSort(dataset.copy()))
    algs.append(RadixSort(dataset.copy()))
    return algs


def random_arr(size, lenght):
    return [randint(0, size) for i in range(0, lenght)]


print(intros[randint(0, len(intros) - 1)])

array = random_arr(500, 100)
algorithms = init_algs(array)
dataset = {}
axs = []
index = [j for j in range(0, len(array))]
threads = []
figure = plt.figure()

for i in range(1, len(algorithms) + 1):
    axs.append(figure.add_subplot(2, 5, i))

for i in range(0, len(algorithms)):
    threads.append(Thread(target=algorithms[i].sort))


def animate():
    for a in algorithms:
        dataset[type(a).__name__] = a.arr
    for i in range(0, len(axs)):
        axs[i].clear()
        axs[i].set_title(algorithms[i].__class__.__name__)
        axs[i].bar(index, dataset[algorithms[i].__class__.__name__])


animation.FuncAnimation(figure, animate, interval=10)

for thread in threads:
    thread.start()

plt.show()

