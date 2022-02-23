from PyQt5.QtCore import Qt, QSize,pyqtSlot, QRunnable, QThreadPool, QTimer
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget

from .controller_input import ControllerInput
from .graph import CustomGraph
from server import Comms    


class Worker(QRunnable):
    '''
    Worker thread

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run code

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PID Tuning App")
        self.setMinimumSize(QSize(1280,720))

        left_widgets = []

        self.threadpool = QThreadPool()
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

        self.comms = None
        vars = self.init_receive_thread()
        self.graphs = [CustomGraph(name) for name in vars]
        self.comms.graphs = self.graphs
        for graph in self.graphs:
            right_layout.addWidget(graph)
        
        layout.addLayout(left_layout,stretch=1)
        layout.addLayout(right_layout,stretch=1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def init_receive_thread(self):
        self.comms = Comms()
        self.header_msg = self.comms.receive_header()
        while not(self.header_msg):
            self.header_msg = self.comms.receive_header()
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.comms.receive_data)
        self.timer.start()
        return self.header_msg

    def init_transfer_thread(self):
        #worker = 
        return

