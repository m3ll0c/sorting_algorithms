"""
" Este arquivo contém a interface que será utilizada e implementada pelas classes de ordenação
" Procura-se por meio desta interface abstrair as funções básicas que a aplicação espera do algoritmo
" Author: Gabriel Melo
"""

class SortAlgorithm(object):

    # retorna o dataset
    def sort(self):
        raise NotImplementedError

    def is_sorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True
