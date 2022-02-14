import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PID Tuning App")
window.setFixedWidth(1000)
#window.setStyleSheet("background:")

grid = QGridLayout()

window.setLayout(grid)

window.show()
sys.exit(app.exec())