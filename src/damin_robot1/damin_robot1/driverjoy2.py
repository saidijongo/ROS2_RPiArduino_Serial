import minimalmodbus
import time

# Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Serial port parameters
SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 115200
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8

# Motor control addresses
CONTROL_MODE_ADDR = 0x200D
LEFT_MOTOR_VELOCITY_ADDR = 0x208E
RIGHT_MOTOR_VELOCITY_ADDR = 0x208F

# Control mode values
VELOCITY_MODE = 0x03

left_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)
right_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)

left_motor.serial.baudrate = BAUDRATE
left_motor.serial.bytesize = BYTESIZE
left_motor.serial.parity = PARITY
left_motor.serial.stopbits = STOPBITS

right_motor.serial.baudrate = BAUDRATE
right_motor.serial.bytesize = BYTESIZE
right_motor.serial.parity = PARITY
right_motor.serial.stopbits = STOPBITS

def rotate_motors(left_speed, right_speed):
    print("Rotating motors. Left Speed:", left_speed, "Right Speed:", right_speed)
    # Set control mode to velocity mode
    left_motor.write_register(CONTROL_MODE_ADDR, VELOCITY_MODE, functioncode=6)
    right_motor.write_register(CONTROL_MODE_ADDR, VELOCITY_MODE, functioncode=6)

    left_motor.write_register(LEFT_MOTOR_VELOCITY_ADDR, left_speed, functioncode=6)
    right_motor.write_register(RIGHT_MOTOR_VELOCITY_ADDR, right_speed, functioncode=6)

def stop_motors():
    print("Stopping motors.")
    left_motor.write_register(CONTROL_MODE_ADDR, 0x00, functioncode=6)
    right_motor.write_register(CONTROL_MODE_ADDR, 0x00, functioncode=6)

try:
    rotate_motors(50, 50)
    time.sleep(5)

    rotate_motors(75, 75)
    time.sleep(5)

    stop_motors()

except Exception as e:
    print("Error:", e)

finally:
    stop_motors()



"""
import minimalmodbus
import time

# Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Serial port parameters
SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 115200
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8

# Motor control addresses
CONTROL_MODE_ADDR = 0x200D
LEFT_MOTOR_VELOCITY_ADDR = 0x208E
RIGHT_MOTOR_VELOCITY_ADDR = 0x208F

# Control mode values
VELOCITY_MODE = 0x03

# Create instruments for left and right motors
left_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)
right_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)

# Configure serial port parameters
left_motor.serial.baudrate = BAUDRATE
left_motor.serial.bytesize = BYTESIZE
left_motor.serial.parity = PARITY
left_motor.serial.stopbits = STOPBITS

right_motor.serial.baudrate = BAUDRATE
right_motor.serial.bytesize = BYTESIZE
right_motor.serial.parity = PARITY
right_motor.serial.stopbits = STOPBITS

# Function to rotate both motors
def rotate_motors(left_speed, right_speed):
    # Set control mode to velocity mode
    left_motor.write_register(CONTROL_MODE_ADDR, VELOCITY_MODE, functioncode=6)
    right_motor.write_register(CONTROL_MODE_ADDR, VELOCITY_MODE, functioncode=6)

    # Set velocities for left and right motors
    left_motor.write_register(LEFT_MOTOR_VELOCITY_ADDR, left_speed, functioncode=6)
    right_motor.write_register(RIGHT_MOTOR_VELOCITY_ADDR, right_speed, functioncode=6)

# Function to stop both motors
def stop_motors():
    # Set control mode to stop
    left_motor.write_register(CONTROL_MODE_ADDR, 0x00, functioncode=6)
    right_motor.write_register(CONTROL_MODE_ADDR, 0x00, functioncode=6)

try:
    # Rotate both motors forward at 50% speed
    rotate_motors(50, 50)
    time.sleep(5)  # Keep motors running for 5 seconds

    # Rotate left motor forward and right motor backward at 75% speed
    rotate_motors(75, 75)
    time.sleep(5)

    # Stop both motors
    stop_motors()

except Exception as e:
    print("Error:", e)

finally:
    stop_motors()
"""