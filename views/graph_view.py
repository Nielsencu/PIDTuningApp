import pyqtgraph as pg

class GraphView(pg.PlotWidget):
    def __init__(self,name):
        self.setTitle(name, color="b", size="30pt")
        self.x = []
        self.y = []
    
    def start(self):
        self.data_line = self.plot(self.x, self.y,pen=self.pen)

    def setup(self,controller):
        self.controller = controller

        # Styling
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.setBackground('w')

    def set_pen(self, pen):
        self.pen = pg.mkPen(color=pen)

    def update_plot(self):
        self.data_line.setData(self.x, self.y)