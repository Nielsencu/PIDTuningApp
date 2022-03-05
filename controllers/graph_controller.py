import random
from abc import ABC, abstractmethod
class Strategy:
    @abstractmethod
    def update_model(self, model, data):
        pass
    @abstractmethod
    def update_view(self, view, model):
        pass

class ShiftStrategy:
    def update_model(self, model ,data):
        model.x = model.x[1:]
        if not(model.x):
            last_x = -1
        else:
            last_x = model.x[-1]
        model.x.append(last_x + 1)

        model.y = model.y[1:]
        model.y.append(data)

    def update_view(self, view, model):
        view.x = view.x[1:]
        view.x.append(model.x[-1])

        view.y = view.y[1:]
        view.y.append(model.y[-1])
class AppendStrategy:
    def update_model(self, model, data):
        if not(model.x):
            last_x = -1
        else:
            last_x = model.x[-1]
        model.x.append(last_x + 1)
        model.y.append(data)

    def update_view(self, view, model):
        view.x.append(model.x[-1])
        view.y.append(model.y[-1])

class GraphController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.update = True

    def start(self):
        self.view.setup(self, self.model.name)

    def update_graph(self, data):
        if len(self.model.x) < 100:
            strategy = AppendStrategy()
        else:
            strategy = ShiftStrategy()
        strategy.update_model(self.model, data)
        strategy.update_view(self.view, self.model)

        # Updates graph view
        self.view.update_plot()

    def toggle_update(self):
        self.update = not(self.update)

    def handle_data(self,data):
        if self.update:
            self.update_graph(data)

    def get_view(self):
        return self.view

class GraphFactory:
    def __init__(self):
        self.loggers = []

    def create_graph_controllers(self,graphs):
        for view,model in graphs:
            self.loggers.append(GraphController(view,model))
        return self

    def build(self):
        return self.loggers

class GraphManager:
    def setup(self, graph_controllers):
        self.graph_controllers = graph_controllers
        for controllers in self.graph_controllers:
            controllers.start()

    def get_graph_controller(self, i: int) -> GraphController:
        return self.graph_controllers[i]

    def handle_data(self, data):
        for i in range(len(self.graph_controllers)):
            self.get_graph_controller(i).handle_data(data[i])
    


