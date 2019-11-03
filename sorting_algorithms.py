"""
    Scriptoso da massa
    Author: Gabriel Melo
"""
import os
import signal
import sys

from algorithms.SelectionSort import SelectionSort
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
from threading import Thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import argparse

def init_algs(dataset, timeout):
    algs = list()
    algs.append(InsertionSort(dataset.copy(), timeout))
    algs.append(BubbleSort(dataset.copy(), timeout))
    algs.append(BogoSort(dataset.copy(), timeout))
    algs.append(CountingSort(dataset.copy(), timeout))
    algs.append(HeapSort(dataset.copy(), timeout))
    algs.append(MergeSort(dataset.copy(), timeout))
    algs.append(PancakeSort(dataset.copy(), timeout))
    algs.append(QuickSort(dataset.copy(), timeout))
    algs.append(RadixSort(dataset.copy(), timeout))
    algs.append(SelectionSort(dataset.copy(), timeout))
    return algs


def animate(i):
    dataset = {}
    for a in algorithms:
        dataset[type(a).__name__] = a.arr
    for j in range(0, len(axs)):
        axs[j].clear()
        axs[j].set_title(algorithms[j].__class__.__name__)
        axs[j].bar([k+1 for k in range(0, len(dataset[algorithms[j].__class__.__name__]))],
                   dataset[algorithms[j].__class__.__name__])


def random_arr(size, lenght):
    return [randint(0, size) for i in range(0, lenght)]


def init_args():
    print(intros[randint(0, len(intros) - 1)])
    parser = argparse.ArgumentParser(
        description="Programa que reune algoritmos de ordenação estudados em CC e permite sua visualização",
        usage="sorting_algorithms.py --size [N] --range [G] --timeout [M]")
    parser.add_argument('-l', '--lenght', metavar='N', type=int,
                        help='Size of the dataset. Default is 50.', default=50)
    parser.add_argument('-s', '--size', metavar='G', type=int,
                        help='Maximum value in the dataset. Default is 500.', default=500)
    parser.add_argument('-t', '--timeout', metavar='M', type=int,
                        help='Sleep between the iterations, every class has the same coefficient. Default is 20',
                        default=20)
    args = parser.parse_args()
    return args.size, args.lenght, args.timeout


if __name__ == "__main__":
    size, lenght, timeout = init_args()
    array = random_arr(size, lenght)
    algorithms = init_algs(array, timeout)
    figure = plt.figure()
    axs = []
    threads = []

    for i in range(1, len(algorithms) + 1):
        axs.append(figure.add_subplot(2, 5, i))

    for i in range(0, len(algorithms)):
        threads.append(Thread(target=algorithms[i].sort))

    for thread in threads:
        thread.start()

    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()

    ani = animation.FuncAnimation(figure, animate, interval=timeout)

    plt.show()
    plt.close(figure)

    os.kill(os.getpid(), signal.SIGINT)
