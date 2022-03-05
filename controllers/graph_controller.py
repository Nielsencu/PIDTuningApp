import random

class GraphController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.init_graph()

    def start(self):
        self.view.setup(self)

    def init_graph(self):
        for i in range(1,101):
            self.model.x.append(i)
            self.model.y.append(random.randint(0,100))
            self.view.x.append(self.model.x[-1])
            self.view.y.append(self.model.y[-1])

    def update_graph(self, data):
        # Updates model
        self.model.x = self.model.x[1:]
        self.model.x.append(self.model.x[-1] + 1)

        self.model.y = self.model.y[1:]
        self.model.y.append(data)

        # Updates view by consuming data from model
        self.view.x = self.view.x[1:]
        self.view.x.append(self.model.x[-1])

        self.view.y = self.view.y[1:]
        self.view.y.append(self.model.y[-1])

        # Updates graph view
        self.view.update_plot()
