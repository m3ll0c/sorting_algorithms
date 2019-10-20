import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class View:

    def __init__(self, controller, timeout=1000):
        self.controller = controller
        self.timeout = timeout/1000

    def show(self):
        while True:
            self.controller.iter_all()
            for d in self.controller.currentDatasets:
                print(d + " " + str(self.controller.currentDatasets[d]))
            print('\n')
            time.sleep(self.timeout)

    def update_graphs(self):
        pass

    def init_graphs(self):
        pass