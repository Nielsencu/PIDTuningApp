from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget

from .controller_input import ControllerInput

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PID Tuning App")
        self.setMinimumSize(QSize(1280,720))

        left_widgets = []

        ctrl_inputs = [ControllerInput(controller_type +":") for controller_type in "PID"]

        for ctrl in ctrl_inputs:
            for w in ctrl.widgets:
                left_widgets.append(w)

        layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignTop)

        for w in left_widgets:
            left_layout.addWidget(w,stretch=1)
        
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignTop)


        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget2 = pg.PlotWidget()
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget1.plot(hour, temperature,pen=pen)
        self.graphWidget1.setTitle("Motor Position", color="b", size="30pt")
        self.graphWidget2.plot(hour, temperature,pen=pen)
        self.graphWidget2.setTitle("Motor RPM", color="b", size="30pt")
        self.graphWidget1.setBackground('w')
        self.graphWidget2.setBackground('w')
        right_layout.addWidget(self.graphWidget1)
        right_layout.addWidget(self.graphWidget2)

        layout.addLayout(left_layout,stretch=1)
        layout.addLayout(right_layout,stretch=1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)