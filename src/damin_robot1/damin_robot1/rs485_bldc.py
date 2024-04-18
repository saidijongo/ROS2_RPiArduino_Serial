
import minimalmodbus
import time

ser = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # Port name, slave address (1 is default)

ser.serial.baudrate = 115200
ser.serial.bytesize = 8
ser.serial.parity = minimalmodbus.serial.PARITY_NONE
ser.serial.stopbits = 1
ser.serial.timeout = 0.05 

#register addresses
CONTROL_WORD_ADDRESS = 0x200E
TARGET_VELOCITY_LEFT_ADDRESS = 0x2088
TARGET_VELOCITY_RIGHT_ADDRESS = 0x2089

try:
    # Quick stop
    ser.write_register(CONTROL_WORD_ADDRESS, 0x0005, functioncode=6)

    # Set target velocity for left motor
    ser.write_register(TARGET_VELOCITY_LEFT_ADDRESS, 100, functioncode=6)

    # Set target velocity for right motor
    ser.write_register(TARGET_VELOCITY_RIGHT_ADDRESS, 100, functioncode=6)

    time.sleep(1)

    # Stop motors
    ser.write_register(CONTROL_WORD_ADDRESS, 0x0007, functioncode=6)

except Exception as e:
    print("Error:", e)



''' 
from modbus_tk import modbus_rtu
import serial
import time  # Import time module for delays
from inputs import get_gamepad  # Import function to read gamepad inputs

# Define the serial port
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)  # Set baudrate directly during serial port initialization

# Create a Modbus RTU client
master = modbus_rtu.RtuMaster(ser)

# Set the communication parameters
master.set_timeout(5.0)

# Define register addresses
CONTROL_WORD_ADDRESS = 0x200E
CONTROL_MODE_ADDRESS = 0x200D
ACCELERATION_TIME_LEFT_ADDRESS = 0x2080
ACCELERATION_TIME_RIGHT_ADDRESS = 0x2081
DECELERATION_TIME_LEFT_ADDRESS = 0x2082
DECELERATION_TIME_RIGHT_ADDRESS = 0x2083
TARGET_VELOCITY_LEFT_ADDRESS = 0x2088
TARGET_VELOCITY_RIGHT_ADDRESS = 0x2089
ACTUAL_VELOCITY_LEFT_ADDRESS = 0x20AB
ACTUAL_VELOCITY_RIGHT_ADDRESS = 0x20AC

# Velocity mode initialization
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, CONTROL_WORD_ADDRESS, output_value=0x0005)  # Quick stop
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, CONTROL_MODE_ADDRESS, output_value=0x0003)   # Velocity mode
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, ACCELERATION_TIME_LEFT_ADDRESS, output_value=500)  # Acceleration time (Left)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, ACCELERATION_TIME_RIGHT_ADDRESS, output_value=500) # Acceleration time (Right)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, DECELERATION_TIME_LEFT_ADDRESS, output_value=500)  # Deceleration time (Left)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, DECELERATION_TIME_RIGHT_ADDRESS, output_value=500) # Deceleration time (Right)

try:
    while True:
        gamepad = get_gamepad()

        if gamepad["a"]:
            # Increase motor speed
            master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, TARGET_VELOCITY_LEFT_ADDRESS, output_value=1000)
        elif gamepad["b"]:
            # Decrease motor speed
            master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, TARGET_VELOCITY_LEFT_ADDRESS, output_value=500)
        elif gamepad["lt"] > 0:
            # Change motor direction (Left)
            master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=1)
        elif gamepad["rt"] > 0:
            # Change motor direction (Right)
            master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=0)

        # Read actual velocity for left motor
        actual_velocity_left = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, ACTUAL_VELOCITY_LEFT_ADDRESS, 1)
        print("Actual Velocity (Left):", actual_velocity_left[0])

        # Read actual velocity for right motor
        actual_velocity_right = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, ACTUAL_VELOCITY_RIGHT_ADDRESS, 1)
        print("Actual Velocity (Right):", actual_velocity_right[0])

        # Delay for stability
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
'''

#New code####################
'''
from modbus_tk import modbus_rtu
import serial
import time  # Import time module for delays
from inputs import get_gamepad  # Import function to read gamepad inputs

# Define the serial port
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)  # Set baudrate directly during serial port initialization

# Create a Modbus RTU client
master = modbus_rtu.RtuMaster(ser)

# Set the communication parameters
master.set_timeout(5.0)

# Define register addresses
CONTROL_WORD_ADDRESS = 0x200E
CONTROL_MODE_ADDRESS = 0x200D
ACCELERATION_TIME_LEFT_ADDRESS = 0x2080
ACCELERATION_TIME_RIGHT_ADDRESS = 0x2081
DECELERATION_TIME_LEFT_ADDRESS = 0x2082
DECELERATION_TIME_RIGHT_ADDRESS = 0x2083
TARGET_VELOCITY_LEFT_ADDRESS = 0x2088
TARGET_VELOCITY_RIGHT_ADDRESS = 0x2089
ACTUAL_VELOCITY_LEFT_ADDRESS = 0x20AB
ACTUAL_VELOCITY_RIGHT_ADDRESS = 0x20AC

# Velocity mode initialization
master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, CONTROL_WORD_ADDRESS, output_value=0x0005)  # Quick stop
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, CONTROL_MODE_ADDRESS, output_value=0x0003)   # Velocity mode
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, ACCELERATION_TIME_LEFT_ADDRESS, output_value=500)  # Acceleration time (Left)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, ACCELERATION_TIME_RIGHT_ADDRESS, output_value=500) # Acceleration time (Right)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, DECELERATION_TIME_LEFT_ADDRESS, output_value=500)  # Deceleration time (Left)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, DECELERATION_TIME_RIGHT_ADDRESS, output_value=500) # Deceleration time (Right)

try:
    while True:
        gamepad = get_gamepad()

        if gamepad["a"]:
            # Increase motor speed
            master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, TARGET_VELOCITY_LEFT_ADDRESS, output_value=1000)
        elif gamepad["b"]:
            # Decrease motor speed
            master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, TARGET_VELOCITY_LEFT_ADDRESS, output_value=500)
        elif gamepad["lt"] > 0:
            # Change motor direction (Left)
            master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=1)
        elif gamepad["rt"] > 0:
            # Change motor direction (Right)
            master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=0)

        # Read actual velocity for left motor
        actual_velocity_left = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, ACTUAL_VELOCITY_LEFT_ADDRESS, 1)
        print("Actual Velocity (Left):", actual_velocity_left[0])

        # Read actual velocity for right motor
        actual_velocity_right = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, ACTUAL_VELOCITY_RIGHT_ADDRESS, 1)
        print("Actual Velocity (Right):", actual_velocity_right[0])

        # Delay for stability
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

'''

###################New code##########
'''
import serial
from modbus_tk import modbus_rtu
from modbus_tk.defines import WRITE_SINGLE_REGISTER, READ_INPUT_REGISTERS, READ_COILS

# Define the serial port with the specified baud rate
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Create a Modbus RTU client
master = modbus_rtu.RtuMaster(ser)

# Set the timeout
master.set_timeout(5.0)

# Write to holding register to control motor speed
master.execute(1, WRITE_SINGLE_REGISTER, 0, output_value=500)

# Read input register to get motor status
status = master.execute(1, READ_INPUT_REGISTERS, 0, 1)

# Read coil to toggle motor direction
direction = master.execute(1, READ_COILS, 0, 1)

gamepad = get_gamepad()
if gamepad['button_A']:
    # Increase motor speed
    master.execute(1, WRITE_SINGLE_REGISTER, 0, output_value=1000)
elif gamepad['button_B']:
    # Decrease motor speed
    master.execute(1, WRITE_SINGLE_REGISTER, 0, output_value=500)
elif gamepad['left_trigger'] > 0:
    # Change motor direction
    master.execute(1, WRITE_SINGLE_COIL, 0, output_value=1)
elif gamepad['right_trigger'] > 0:
    # Change motor direction
    master.execute(1, WRITE_SINGLE_COIL, 0, output_value=0)



#######New code

import serial
from modbus_tk import modbus_rtu

# Define the serial port with the specified baud rate
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Create a Modbus RTU client
master = modbus_rtu.RtuMaster(ser)

# Set the timeout
master.set_timeout(5.0)

# Write to holding register to control motor speed
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, 0, output_value=500)

# Read input register to get motor status
status = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, 0, 1)

# Read coil to toggle motor direction
direction = master.execute(1, modbus_rtu.READ_COILS, 0, 1)

gamepad = get_gamepad()
if gamepad['button_A']:
    # Increase motor speed
    master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, 0, output_value=1000)
elif gamepad['button_B']:
    # Decrease motor speed
    master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, 0, output_value=500)
elif gamepad['left_trigger'] > 0:
    # Change motor direction
    master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=1)
elif gamepad['right_trigger'] > 0:
    # Change motor direction
    master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=0)

'''


###New code
''' 
from modbus_tk import modbus_rtu
#from modbus_tk.defines import SerialPort
#from modbus_tk.defines import ModbusSerialPort
#from modbus_tk.defines import SerialPort
import serial


# Define the serial port
#ser = SerialPort("/dev/ttyUSB0")
ser = serial.Serial("/dev/ttyUSB0")

# Create a Modbus RTU client
master = modbus_rtu.RtuMaster(ser)

# Set the communication parameters
master.set_timeout(5.0)
master.set_baudrate(115200)


# Write to holding register to control motor speed
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, 0, output_value=500)

# Read input register to get motor status
status = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, 0, 1)

# Read coil to toggle motor direction
direction = master.execute(1, modbus_rtu.READ_COILS, 0, 1)


gamepad = get_gamepad()
if gamepad['button_A']:
    # Increase motor speed
    master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, 0, output_value=1000)
elif gamepad['button_B']:
    # Decrease motor speed
    master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, 0, output_value=500)
elif gamepad['left_trigger'] > 0:
    # Change motor direction
    master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=1)
elif gamepad['right_trigger'] > 0:
    # Change motor direction
    master.execute(1, modbus_rtu.WRITE_SINGLE_COIL, 0, output_value=0)

'''


