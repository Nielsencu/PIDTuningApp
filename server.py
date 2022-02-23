import serial
import time
import struct
import random
from views.logger import Logger
import os
class Comms():
    def __init__(self):
        self.ser = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
        time.sleep(2)
        self.BINARY_HEADERSTRFORMAT = ""
        self.BINARY_STRFORMAT = ""
        self.variables = []
        self.graphs = []
        self.loggers = []
        self.num_var = 0
        self.log_folder = 'log/'
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

    def receive_header(self):
        # packet = self.ser.read(struct.calcsize(self.BINARY_HEADERSTRFORMAT))
        # num_var = packet[0]
        self.variables = [i for i in "ABCDEF"]
        #for var in num_var:
        #    variables.append(var)
        self.BINARY_STRFORMAT = "HHfHHH"
        self.num_var = len(self.variables)
        self.loggers = [Logger(self.log_folder, self.variables[i]) for i in range(self.num_var)]
        # Add header to log
        for i in range(self.num_var):
            self.loggers[i].addRow((self.variables[i], "column"))
        return self.variables
        

    def receive_data(self):
        packet = self.ser.read(struct.calcsize(self.BINARY_STRFORMAT))
        tuple_packet = struct.unpack(self.BINARY_STRFORMAT,packet)
        
        for i in range(self.num_var):
            data = random.randint(0,100)
            self.graphs[i].updatePlotData(data)
            self.loggers[i].addRow((data,1))
            #self.graphs[i].updatePlotData(tuple_packet[i])


    def transfer_data(self):
        return
