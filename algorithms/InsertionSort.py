"""
"
" Author: Gabriel Melo
"""

from algorithms.SortAlgorithm import SortAlgorithm as Parent


class InsertionSort(Parent):

    def next_iteration(self):
        print(self.dataset)

    def iteration(self):
        pass

    def sort(self):
        pass

    # Embora pareça desnecessário, a implementação desse método permite que alguma formatação seja feita
    def get_dataset(self):
        return self.dataset
