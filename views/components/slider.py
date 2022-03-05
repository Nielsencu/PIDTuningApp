from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSlider

class Slider(QSlider):

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

class DoubleSlider(Slider):
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