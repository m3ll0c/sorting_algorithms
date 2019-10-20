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
from random import randint, sample
from threading import Thread

def init_algs(dataset):
    algs = list()
    algs.append(InsertionSort(dataset.copy()))
    algs.append(BubbleSort(dataset.copy()))
    algs.append(BogoSort(dataset.copy()))
    return algs


def main():
    print(intros[randint(0, len(intros) - 1)])
    arr = sample(range(10), 10)
    view = View(Controller(init_algs(arr)), timeout=1000)
    view.show()


if __name__ == '__main__':
    main()
