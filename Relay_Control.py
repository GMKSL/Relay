import serial
import sys

arduino_port = '/dev/ttyACM0'  # Replace with the actual serial port
baud_rate = 9600

def send_command(command):
    ser.write(command.encode())


def Relay_Control_Function(Relay_no,State):
    if(State=="OFF"):
        State=0
        user_input=str(Relay_no)+str(State)
    if(State=="ON"):
        State=1
        user_input=str(Relay_no)+str(State)
# Create a global serial connection if it doesn't exist
    if 'ser' not in globals():
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    if user_input == '11' or user_input == '10'  or user_input == '21'  or user_input == '20' or user_input == '31'  or user_input == '30' or user_input == '41'  or user_input == '40' or user_input == '51' or user_input == '50' or user_input == '61'  or user_input == '60' or user_input == '71'  or user_input == '70' or user_input == '81'  or user_input == '80':
    	ser.write(user_input.encode())
    	#send_command(user_input)

