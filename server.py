import serial
import time
import struct
import random
from views.logger import Logger, LoggerManager
import os
class SerialConnection:
    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
        time.sleep(2)
        self.BINARY_HEADERSTRFORMAT = ""
        self.BINARY_STRFORMAT = ""
        self.variables = []
        self.num_var = 0
        self.log_manager = LoggerManager()
        #self.graph_manager = GraphManager()

    def receive_header(self):
        # packet = self.ser.read(struct.calcsize(self.BINARY_HEADERSTRFORMAT))
        # num_var = packet[0]
        self.variables = [i for i in "ABCDEF"]
        self.BINARY_STRFORMAT = "HHfHHH"
        self.log_manager.process_header(self.variables)
        return self.variables

    def receive_data(self):
        packet = self.ser.read(struct.calcsize(self.BINARY_STRFORMAT))
        tuple_packet = struct.unpack(self.BINARY_STRFORMAT,packet)

        tuple_packet = tuple(random.randomint(0,100) for i in range(len(tuple_packet)))

        self.log_manager.process_data(tuple_packet)
        #self.graph_manager.process_data(tuple_packet)


    def transfer_data(self):
        return
