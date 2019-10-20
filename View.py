"""
    Author: Gabriel Melo
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class View:

    def __init__(self, controller, timeout=1000):
        self.controller = controller
        self.fig = plt.figure()
        self.axs = []
        self.ani = None
        self.timeout = timeout

    def animate(self, i):
        self.controller.iter_all()
        for i in range(0, len(self.axs)):
            index = []
            values = self.controller.currentDatasets[self.controller.algorithms[i].__class__.__name__].copy()
            [index.append(i) for i in range(0, len(values))]
            self.axs[i].clear()
            self.axs[i].set_title(self.controller.algorithms[i].__class__.__name__)
            self.axs[i].bar(index, values)

    def build_graphics(self):
        for i in range(1, len(self.controller.algorithms) + 1):
            self.axs.append(self.fig.add_subplot(2, 5, i))

    def run(self, maximised=True):
        self.build_graphics()
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=self.timeout)
        if maximised:
            mng = plt.get_current_fig_manager()
            mng.window.showMaximized()
        plt.show()