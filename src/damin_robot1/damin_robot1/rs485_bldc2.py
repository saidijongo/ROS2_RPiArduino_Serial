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



##########New code ########
from modbus_tk import modbus_rtu
import serial

# Define the serial port
ser = serial.Serial("/dev/ttyUSB0")

# Create a Modbus RTU client
master = modbus_rtu.RtuMaster(ser)

# Set the communication parameters
master.set_timeout(5.0)
master.set_baudrate(115200)

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

# Set target velocity for left motor to 100 RPM
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, TARGET_VELOCITY_LEFT_ADDRESS, output_value=1000)

# Read actual velocity for left motor
actual_velocity_left = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, ACTUAL_VELOCITY_LEFT_ADDRESS, 1)
print("Actual Velocity (Left):", actual_velocity_left[0])

# Set target velocity for right motor to -100 RPM (reverse direction)
master.execute(1, modbus_rtu.WRITE_SINGLE_REGISTER, TARGET_VELOCITY_RIGHT_ADDRESS, output_value=-1000)

# Read actual velocity for right motor
actual_velocity_right = master.execute(1, modbus_rtu.READ_INPUT_REGISTERS, ACTUAL_VELOCITY_RIGHT_ADDRESS, 1)
print("Actual Velocity (Right):", actual_velocity_right[0])
'''