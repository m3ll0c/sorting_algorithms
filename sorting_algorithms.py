"""
" Ponto de entrada do programa
" Author: Gabriel Melo
"""

from intro import intros
from Controller import Controller
from View import View
from algorithms.InsertionSort import InsertionSort
from algorithms.BubbleSort import BubbleSort
from algorithms.BogoSort import BogoSort
from algorithms.CountingSort import CountingSort
from random import randint


def init_algs(dataset):
    algs = list()
    algs.append(InsertionSort(dataset.copy()))
    algs.append(BubbleSort(dataset.copy()))
    algs.append(BogoSort(dataset.copy()))
    algs.append(CountingSort(dataset.copy()))
    return algs


def random_arr(size, lenght):
    return [randint(0, size) for i in range(0, lenght)]


def main():
    print(intros[randint(0, len(intros) - 1)])
    arr = random_arr(500, 50)
    view = View(Controller(init_algs(arr)), timeout=40)
    view.run()


if __name__ == '__main__':
    main()
