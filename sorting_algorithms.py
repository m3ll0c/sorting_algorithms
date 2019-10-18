"""
" Ponto de entrada do programa
" Author: Gabriel Melo
"""

from algorithms.InsertionSort import InsertionSort
from algorithms.BubbleSort import BubbleSort
from algorithms.BogoSort import BogoSort


def main():
    arr = [0, 4, 5, 2, 1]

    insert2 = InsertionSort(arr)
    insert2.sort()
    print(insert2.arr)

    bubb2 = BubbleSort(arr)
    bubb2.sort()
    print(bubb2.arr)

    bog = BogoSort(arr)
    bog.sort(1000)  # chama a função que possui um limite de iterações
    print(bog.arr)


if __name__ == '__main__':
    main()
