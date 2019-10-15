"""
" Este arquivo contém a interface que será utilizada e implementada pelas classes de ordenação
" Procura-se por meio desta interface abstrair as funções básicas que a aplicação espera do algoritmo
" Author: Gabriel Melo
"""


class SortAlgorithm():

    def __init__(self, dataset):
        self.dataset = dataset

    # executa uma iteração
    def next_iteration(self):
        pass

    # contém a implementação da lógica da ordenação
    def iteration(self):
        pass

    # retorna o dataset
    def get_dataset(self):
        return self.dataset