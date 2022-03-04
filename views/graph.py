from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import random

    

class CustomGraph(pg.PlotWidget):
    def __init__(self, name):
        super().__init__()
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.setTitle(name, color="b", size="30pt")
        self.setBackground('w')
        self.x = [i for i in range(1,101)]
        self.y = [random.randint(0,100) for i in range(0,100)]
        self.data_line = self.plot(self.x, self.y,pen=self.pen)

    def set_pen(self, pen):
        self.pen = pg.mkPen(color=pen)

    def update_plot(self, newPoint):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y.append(newPoint)
        self.data_line.setData(self.x, self.y)
    
        