"""
" Ponto de entrada do programa
" Author: Gabriel Melo
"""

from algorithms.InsertionSort import InsertionSort


def main():
    ins = InsertionSort([1, 2])
    ins.next_iteration()
    ins.get_dataset()


if __name__ == '__main__':
    main()