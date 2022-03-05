from PyQt5.QtWidgets import QLineEdit

class InputField(QLineEdit):
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