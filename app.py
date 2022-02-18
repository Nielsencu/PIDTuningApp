import sys

from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QMenu, QSlider

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class QCustomLabel(QLabel):
    def __init__(self, text):
        super().__init__()
        self.initText = text
        super().setText(text)

    def setText(self,text):
        text = self.initText + str(text)
        super().setText(text)

class QCustomInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.label = None
        self.slider= None

    def attachSlider(self,slider):
        self.slider = slider

    def attachLabel(self,label):
        self.label = label

    def onEditingFinished(self):
        self.label.setText(self.displayText())
        self.slider.setValue(int(self.displayText()))

class QCustomSlider(QSlider):

    def __init__(self, orientation):
        super().__init__(orientation)
        self.label = None
        self.input = None

    def attachInput(self,input):
        self.input = input

    def attachLabel(self,label):
        self.label = label

    def onValueChanged(self,value):
        self.label.setText(value)
        self.input.setText(str(value))

class QCustomDoubleSlider(QCustomSlider):
    doubleValueChanged = pyqtSignal(float)

    def __init__(self,orientation, decimals=4):
        super().__init__(orientation)
        self.multi = 10 ** decimals
        self.valueChanged.connect(self.emitDoubleValueChanged)

    def emitDoubleValueChanged(self):
        value = float(super().value())/self.multi
        self.doubleValueChanged.emit(value)

    def value(self):
        return float(super().value()) / self.multi

    def setMinimum(self, value):
        return super().setMinimum(int(value * self.multi))

    def setMaximum(self, value):
        return super().setMaximum(int(value * self.multi))

    def setSingleStep(self, value):
        return super().setSingleStep(int(value * self.multi))
    
    def setPageStep(self, value):
        return super().setPageStep(int(value * self.multi))

    def singleStep(self):
        return float(super().singleStep()) / self.multi

    def setValue(self, value):
        super().setValue(int(value * self.multi))

class ControllerInput():
    def __init__(self, ctrl_type):
        self.widgets = []
        self.ctrl_type = ctrl_type
        self.label = QCustomLabel(ctrl_type)
        self.slider = QCustomDoubleSlider(Qt.Horizontal)
        self.input = QCustomInput()
        self.initLabel()
        self.initInput()
        self.initSlider()
    
    def initLabel(self):
        self.label.setStyleSheet("font-size: 12pt;")
        self.label.setFixedHeight(30)
        self.widgets.append(self.label)

    def initSlider(self):
        self.slider.attachInput(self.input)
        self.slider.attachLabel(self.label)
        self.slider.setMinimum(0.0001)
        self.slider.setMaximum(0.1)
        self.slider.setSingleStep(0.0001)
        self.slider.setPageStep(0.005)
        self.slider.doubleValueChanged.connect(self.slider.onValueChanged)
        self.widgets.append(self.slider)

    def initInput(self):
        self.input.attachSlider(self.slider)
        self.input.attachLabel(self.label)
        self.input.editingFinished.connect(self.input.onEditingFinished)
        self.widgets.append(self.input)


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

app = QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec())