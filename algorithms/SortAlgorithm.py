"""
" Este arquivo contém a interface que será utilizada e implementada pelas classes de ordenação
" Procura-se por meio desta interface abstrair as funções básicas que a aplicação espera do algoritmo
" Author: Gabriel Melo
"""

class SortAlgorithm:

    # executa uma iteração
    def next_iteration(self):
        pass

    # contém a implementação da lógica da ordenação
    def iteration(self):
        pass


    def is_sorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True
