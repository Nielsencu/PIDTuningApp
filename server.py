import serial
import time
import struct

ser = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
time.sleep(2)
BINARY_STRFORMAT = "<HHfHHH"
while True:
    packet = ser.read(struct.calcsize(BINARY_STRFORMAT))
    chassis_volt, chassis_current, chassis_power, chassis_power_buffer, shooter_heat0, shooter_heat1 = struct.unpack(BINARY_STRFORMAT,packet)
    print(f'Chassis volt : {chassis_volt}')
    print(f'Chassis current : {chassis_current}')
    print(f'Chassis power : {chassis_power}')
    print(f'Chassis power buffer : {chassis_power_buffer}')
    print(f'Shooter heat0 : {shooter_heat0}')
    print(f'Shooter heat1 : {shooter_heat1}')
