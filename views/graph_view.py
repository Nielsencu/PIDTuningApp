import pyqtgraph as pg

class GraphView(pg.PlotWidget):
    def __init__(self):
        super().__init__()
        self.x = []
        self.y = []
        self.data_line = self.plot(self.x, self.y)
    
    def setup(self,controller, name):
        self.controller = controller
        self.setTitle(name, color="b", size="30pt")

        # Styling
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.setBackground('w')

    def set_pen(self, pen):
        self.pen = pg.mkPen(color=pen)

    def update_plot(self):
        self.data_line.setData(self.x, self.y, pen=self.pen)