from PyQt5.QtCore import Qt
from .input_field import InputField
from .label import Label
from .slider import DoubleSlider

class InputBox():
    def __init__(self, ctrl_type):
        self.widgets = []
        self.ctrl_type = ctrl_type
        self.label = Label(ctrl_type)
        self.slider = DoubleSlider(Qt.Horizontal)
        self.input = InputField()
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