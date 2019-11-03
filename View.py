"""
    Author: Gabriel Melo
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread
import time

class View:

    def __init__(self, algs):
        self.algorithms = algs
        self.fig = plt.figure()
        self.axs = []
        self.threads = []
        [self.threads.append(Thread(target=a.sort)) for a in self.algorithms]
        self.update_datasets = Thread(target=self.update)
        self.update_datasets.start()
        self.datasets = []

    def update(self):
        while True:
            temp = {}
            for a in self.algorithms:
                temp[type(a).__name__] = a.arr.copy()
            print(temp)
            time.sleep(0.25)

    def animate(self, i):
        for i in range(0, len(self.axs)):
            index = []
            values = self.datasets[self.algorithms[i].__class__.__name__]
            [index.append(i) for i in range(0, len(values))]
            self.axs[i].clear()
            self.axs[i].set_title(self.algorithms[i].__class__.__name__)
            self.axs[i].bar(index, values)

    def build_graphics(self):
        for i in range(1, len(self.algorithms) + 1):
            self.axs.append(self.fig.add_subplot(2, 5, i))

    def run(self):
        self.build_graphics()

        plt.get_current_fig_manager().window.showMaximized()
        plt.show()
