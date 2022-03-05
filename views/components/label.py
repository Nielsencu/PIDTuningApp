from PyQt5.QtWidgets import QLabel

class Label(QLabel):
    def __init__(self, text):
        super().__init__()
        self.initText = text
        super().setText(text)

    def setText(self,text):
        text = self.initText + str(text)
        super().setText(text)