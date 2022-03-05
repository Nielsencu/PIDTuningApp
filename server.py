import serial
import time
import struct
import random
from models.logger_model import LoggerModel
from controllers.logger_controller import LoggerManager, LoggerFactory
from controllers.graph_controller import GraphManager

import os
class SerialConnection:
    def __init__(self, port):
        self.ser = serial.Serial(port=port, baudrate=115200, timeout=.1)
        time.sleep(2)
        self.BINARY_HEADERSTRFORMAT = ""
        self.BINARY_STRFORMAT = ""
        self.variables = []
        self.num_var = 0
        self.log_manager = LoggerManager()

    def receive_header(self):
        # packet = self.ser.read(struct.calcsize(self.BINARY_HEADERSTRFORMAT))
        # num_var = packet[0]
        self.motors = ["/motor" + str(i) for i in range(6)]
        self.variables = ["RPM", "Motor position"]
        self.BINARY_STRFORMAT = "HHfHHH"
        self.log_manager.setup(LoggerFactory().create_logger_controllers((LoggerModel() for i in range(len(self.motors)))).set_motors(self.motors).set_folders('log').build())
        self.log_manager.handle_data(self.variables)
        return self.variables

    def receive_data(self):
        packet = self.ser.read(struct.calcsize(self.BINARY_STRFORMAT))
        tuple_packet = struct.unpack(self.BINARY_STRFORMAT,packet)
        tuple_packet = tuple(random.randint(0,100) for i in range(len(self.variables)))
        self.log_manager.handle_data(tuple_packet)
        self.graph_manager.handle_data(tuple_packet)

    def setup_graph(self, graph_controllers):
        self.graph_manager = GraphManager()
        self.graph_manager.setup(graph_controllers)

    def transfer_data(self):
        return
