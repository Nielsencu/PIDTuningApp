import serial
import time
import struct
import random
class Comms():
    def __init__(self):
        self.graphs = []
        self.ser = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
        time.sleep(2)
        self.BINARY_HEADERSTRFORMAT = ""
        self.BINARY_STRFORMAT = "HHfHHH"

    def receive_header(self):
        # packet = self.ser.read(struct.calcsize(self.BINARY_HEADERSTRFORMAT))
        # num_var = packet[0]
        variables = ["Motor Position", "Motor RPM"]
        #for var in num_var:
        #    variables.append(var)
        self.num_var = len(variables)
        return variables
        

    def receive_data(self):
        packet = self.ser.read(struct.calcsize(self.BINARY_STRFORMAT))
        tuple_packet = struct.unpack(self.BINARY_STRFORMAT,packet)
        for i in range(self.num_var):
            self.graphs[i].updatePlotData(random.randint(0,100))
            #self.graphs[i].updatePlotData(tuple_packet[i])
        #chassis_volt, chassis_current, chassis_power, chassis_power_buffer, shooter_heat0, shooter_heat1 = struct.unpack(self.BINARY_STRFORMAT,packet)
        # print(f'Chassis volt : {chassis_volt}')
        # print(f'Chassis current : {chassis_current}')
        # print(f'Chassis power : {chassis_power}')
        # print(f'Chassis power buffer : {chassis_power_buffer}')
        # print(f'Shooter heat0 : {shooter_heat0}')
        # print(f'Shooter heat1 : {shooter_heat1}')
