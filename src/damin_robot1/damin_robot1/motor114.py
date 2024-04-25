import minimalmodbus
import time

#Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# serial port parameters
SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 115200
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8

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

# Function to rotate both motors
def rotate_motors(target_velocity):
    left_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable left motor
    right_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable right motor

    left_motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity for left motor
    right_motor.write_register(0x2089, target_velocity, functioncode=6)  # Set target velocity for right motor

def stop_motors():
    left_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop left motor
    right_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop right motor

try:
    rotate_motors(100)
    time.sleep(10)

    stop_motors()
    time.sleep(1)

except Exception as e:
    print("Error:", e)

finally:
    stop_motors()






###JONGO###
#########################################################################
###New code ### Bueno only left rotation
''' 
import minimalmodbus
import time

# Define the Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Define the serial port parameters
SERIAL_PORT = '/dev/ttyUSB0'  
BAUDRATE = 115200
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8

# Create Modbus instrument objects for left and right motors
left_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)
right_motor = minimalmodbus.Instrument(SERIAL_PORT, RIGHT_MOTOR_ADDRESS)

# Set up serial port parameters
left_motor.serial.baudrate = BAUDRATE
left_motor.serial.bytesize = BYTESIZE
left_motor.serial.parity = PARITY
left_motor.serial.stopbits = STOPBITS

right_motor.serial.baudrate = BAUDRATE
right_motor.serial.bytesize = BYTESIZE
right_motor.serial.parity = PARITY
right_motor.serial.stopbits = STOPBITS

# Function to rotate the motor
def rotate_motor(motor, target_velocity):
    motor.write_register(0x200E, 0x08, functioncode=6)  # Enable
    motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity

# Function to stop the motor
def stop_motor(motor):
    motor.write_register(0x200E, 0x07, functioncode=6)  # Stop

try:
    # Rotate left motor at 100 RPM
    rotate_motor(left_motor, 200)
    time.sleep(5)  # Rotate for 5 seconds

    # Stop left motor
    stop_motor(left_motor)
    time.sleep(1)  # Wait for 1 second

    # Rotate right motor at -100 RPM
    rotate_motor(right_motor, -100)
    time.sleep(2)  # Rotate for 2 seconds

    # Stop right motor
    stop_motor(right_motor)

except Exception as e:
    print("Error:", e)

finally:
    # Ensure motors are stopped before exiting
    stop_motor(left_motor)
    stop_motor(right_motor)

'''

###########################################
#######New code######## no bueno only left deflection


'''
import minimalmodbus

# Define motor driver Modbus slave addresses
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Define Modbus RTU serial port
SERIAL_PORT = '/dev/ttyUSB0' 

# Create Modbus instrument objects for left and right motors
left_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)
right_motor = minimalmodbus.Instrument(SERIAL_PORT, RIGHT_MOTOR_ADDRESS)

# Set communication parameters (baudrate, parity, etc.)
left_motor.serial.baudrate = 115200
left_motor.serial.timeout = 0.1

right_motor.serial.baudrate = 115200 #38400
right_motor.serial.timeout = 0.1

# Function to rotate the motor clockwise
def rotate_clockwise(motor):
    motor.write_register(0, 1)  # Write 1 to control register (start rotation)

# Function to rotate the motor counterclockwise
def rotate_counterclockwise(motor):
    motor.write_register(0, 2)  # Write 2 to control register (start rotation in opposite direction)

# Function to stop the motor
def stop_motor(motor):
    motor.write_register(0, 0)  # Write 0 to control register (stop rotation)

if __name__ == "__main__":
    try:
        # Rotate left motor clockwise for 5 seconds
        rotate_clockwise(left_motor)
        print("Left motor rotating clockwise...")
        time.sleep(5)
        
        # Stop left motor
        stop_motor(left_motor)
        print("Left motor stopped.")
        
        # Rotate right motor counterclockwise for 3 seconds
        rotate_counterclockwise(right_motor)
        print("Right motor rotating counterclockwise...")
        time.sleep(3)
        
        # Stop right motor
        stop_motor(right_motor)
        print("Right motor stopped.")
        
    except Exception as e:
        print("Error:", e)

 ##############################################################################

#New code

import minimalmodbus

# Define Modbus register addresses
CONTROL_MODE_ADDR = 0x200D
LEFT_MOTOR_VELOCITY_ADDR = 0x208E
RIGHT_MOTOR_VELOCITY_ADDR = 0x208F
LEFT_MOTOR_POSITION_ADDR = 0x20AB
RIGHT_MOTOR_POSITION_ADDR = 0x20AC

# Define slave ID
SLAVE_ID = 1

# Create minimalmodbus instrument
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', SLAVE_ID)

# Set control mode (velocity mode)
def set_velocity_mode():
    instrument.write_register(CONTROL_MODE_ADDR, 3, functioncode=6)

# Set motor velocities
def set_motor_velocities(left_velocity, right_velocity):
    instrument.write_register(LEFT_MOTOR_VELOCITY_ADDR, left_velocity, functioncode=6)
    instrument.write_register(RIGHT_MOTOR_VELOCITY_ADDR, right_velocity, functioncode=6)

# Stop motors
def stop_motors():
    set_motor_velocities(0, 0)

# Read motor positions
def read_motor_positions():
    left_position = instrument.read_register(LEFT_MOTOR_POSITION_ADDR, functioncode=3)
    right_position = instrument.read_register(RIGHT_MOTOR_POSITION_ADDR, functioncode=3)
    return left_position, right_position

# Read motor speeds
def read_motor_speeds():
    left_speed = instrument.read_register(LEFT_MOTOR_VELOCITY_ADDR, functioncode=3)
    right_speed = instrument.read_register(RIGHT_MOTOR_VELOCITY_ADDR, functioncode=3)
    return left_speed, right_speed

if __name__ == "__main__":
    # Set velocity mode
    set_velocity_mode()

    # Set motor velocities (100 RPM for both motors)
    set_motor_velocities(100, 100)

    # Read motor positions
    left_position, right_position = read_motor_positions()
    print("Left Motor Position:", left_position)
    print("Right Motor Position:", right_position)

    # Read motor speeds
    left_speed, right_speed = read_motor_speeds()
    print("Left Motor Speed:", left_speed)
    print("Right Motor Speed:", right_speed)

    # Stop motors
    stop_motors()

#################################################################################
import minimalmodbus

# Define the slave address and serial port
SLAVE_ADDRESS = 1
SERIAL_PORT = '/dev/ttyUSB0'

# Define the register addresses and data
REGISTER_START_ADDR = 0x2000  # Start address for left motor encoder wire
NUM_REGISTERS = 2  # Number of registers to write
DATA = [1024, 0]  # Left motor encoder wire and hall offset angle

# Create a minimalmodbus instrument
instrument = minimalmodbus.Instrument(SERIAL_PORT, SLAVE_ADDRESS)

def write_multiple_registers():
    # Write multiple registers
    instrument.write_registers(REGISTER_START_ADDR, DATA)

def main():
    try:
        write_multiple_registers()
        print("Write multiple registers successful")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()


#############################################################################
#New COde

import time
import minimalmodbus

# Define constants
SLAVE_ADDRESS = 1
REGISTER_START_ADDRESS = 0x20
REGISTER_COUNT = 2  # Number of registers to write
COMMAND_TIMEOUT = 1  # Timeout in seconds

# Create instrument object
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', SLAVE_ADDRESS)
instrument.serial.baudrate = 115200
instrument.serial.timeout = COMMAND_TIMEOUT

def write_registers(data):
    """Write multiple registers to the motor driver."""
    try:
        instrument.write_registers(REGISTER_START_ADDRESS, data)
        print("Registers written successfully:", data)
    except Exception as e:
        print("Error writing registers:", e)

def main():
    try:
        # Start communication with the motor driver
        instrument.serial.open()

        # Wait for 10 seconds
        print("Waiting for 10 seconds...")
        time.sleep(10)

        # Run the motors forward
        data = [1024, 0]  # Left motor encoder wire = 1024, hall offset angle = 0
        write_registers(data)
        print("Motors running forward...")

        # Wait for 30 seconds
        print("Running motors forward for 30 seconds...")
        time.sleep(30)

        # Stop the motors
        data = [0, 0]  # Stop command
        write_registers(data)
        print("Motors stopped.")

    except Exception as e:
        print("Error:", e)
    #finally:

    finally:
        # Close communication with the motor driver
        instrument.serial.close()

if __name__ == "__main__":
    main()
'''


'''


import minimalmodbus
import time

# Define the Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

SERIAL_PORT = '/dev/ttyUSB0' 
BAUDRATE = 115200
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8

# Create Modbus instrument objects for left and right motors
left_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)
right_motor = minimalmodbus.Instrument(SERIAL_PORT, RIGHT_MOTOR_ADDRESS)

# Set up serial port parameters
left_motor.serial.baudrate = BAUDRATE
left_motor.serial.bytesize = BYTESIZE
left_motor.serial.parity = PARITY
left_motor.serial.stopbits = STOPBITS

right_motor.serial.baudrate = BAUDRATE
right_motor.serial.bytesize = BYTESIZE
right_motor.serial.parity = PARITY
right_motor.serial.stopbits = STOPBITS

# Function to rotate the motor
def rotate_motor(motor, target_velocity):
    motor.write_register(0x200E, 0x08, functioncode=6)  # Enable
    motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity

# Function to stop the motor
def stop_motor(motor):
    motor.write_register(0x200E, 0x07, functioncode=6)  # Stop

# Function to print current motor positions
def print_current_positions():
    left_position = left_motor.read_register(0x20A7, functioncode=3, signed=True)
    right_position = right_motor.read_register(0x20A9, functioncode=3, signed=True)
    print("Left Motor Position:", left_position)
    print("Right Motor Position:", right_position)

try:
    # Rotate both motors from low speed to high speed
    for speed in range(50, 301, 50):  # Speed range from 50 to 300 RPM
        rotate_motor(left_motor, speed)
        rotate_motor(right_motor, speed)
        time.sleep(5)  # Rotate for 5 seconds
        print_current_positions()

    # Slow down and stop both motors
    for speed in range(300, 49, -50):  # Speed range from 300 to 50 RPM
        rotate_motor(left_motor, speed)
        rotate_motor(right_motor, speed)
        time.sleep(5)  # Rotate for 5 seconds
        print_current_positions()

    # Reverse direction and repeat the process
    for speed in range(50, 301, 50):
        rotate_motor(left_motor, -speed)
        rotate_motor(right_motor, -speed)
        time.sleep(5)  # Rotate for 5 seconds
        print_current_positions()

    # Slow down and stop both motors
    for speed in range(300, 49, -50):
        rotate_motor(left_motor, -speed)
        rotate_motor(right_motor, -speed)
        time.sleep(5)  # Rotate for 5 seconds
        print_current_positions()

except Exception as e:
    print("Error:", e)

finally:
    # Ensure motors are stopped before exiting
    stop_motor(left_motor)
    stop_motor(right_motor)


'''

################################################################################
######New code


'''
import minimalmodbus
import time

# Define the Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Define the serial port parameters
SERIAL_PORT = '/dev/ttyUSB0' 
BAUDRATE = 115200
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8

# Create Modbus instrument objects for left and right motors
left_motor = minimalmodbus.Instrument(SERIAL_PORT, LEFT_MOTOR_ADDRESS)
right_motor = minimalmodbus.Instrument(SERIAL_PORT, RIGHT_MOTOR_ADDRESS)

# Set up serial port parameters
left_motor.serial.baudrate = BAUDRATE
left_motor.serial.bytesize = BYTESIZE
left_motor.serial.parity = PARITY
left_motor.serial.stopbits = STOPBITS

right_motor.serial.baudrate = BAUDRATE
right_motor.serial.bytesize = BYTESIZE
right_motor.serial.parity = PARITY
right_motor.serial.stopbits = STOPBITS

# Set common parameters for both motors
common_params = {
    0x2001: 4,  # RS485 Node ID for both motors
    0x2008: 1000,  # Maximum motor speed for both motors (1000 RPM)
    0x2007: 1,  # Enable the driver when powered on for both motors
}

# Set parameters for left motor
left_motor_params = {
    0x2002: 2,  # RS485 Baud Rate (115200bps) for left motor
}

# Set parameters for right motor
right_motor_params = {
    0x2002: 2,  # RS485 Baud Rate (115200bps) for right motor
}

# Function to rotate the motor
def rotate_motor(motor, target_velocity):
    motor.write_register(0x200E, 0x08, functioncode=6)  # Enable
    motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity

# Function to stop the motor
def stop_motor(motor):
    motor.write_register(0x200E, 0x07, functioncode=6)  # Stop

try:
    # Set common parameters for both motors
    for addr, value in common_params.items():
        left_motor.write_register(addr, value, functioncode=6)
        right_motor.write_register(addr, value, functioncode=6)
        print(f"Set common parameter {addr} to {value} for both motors.")

    # Set left motor specific parameters
    for addr, value in left_motor_params.items():
        left_motor.write_register(addr, value, functioncode=6)
        print(f"Set parameter {addr} to {value} for left motor.")

    # Set right motor specific parameters
    for addr, value in right_motor_params.items():
        right_motor.write_register(addr, value, functioncode=6)
        print(f"Set parameter {addr} to {value} for right motor.")

    # Rotate both motors from low speed to high speed
    for speed in range(100, 1001, 100):  # From 100 RPM to 1000 RPM
        rotate_motor(left_motor, speed)
        rotate_motor(right_motor, speed)
        print(f"Rotating both motors at {speed} RPM.")
        time.sleep(5)  # Rotate for 5 seconds at each speed

    # Slow down and stop both motors
    for speed in range(1000, 0, -100):  # From 1000 RPM to 0 RPM
        rotate_motor(left_motor, speed)
        rotate_motor(right_motor, speed)
        print(f"Slowing down both motors to {speed} RPM.")
        time.sleep(5)  # Rotate for 5 seconds at each speed

    # Rotate both motors in reverse direction
    for speed in range(-100, -1001, -100):  # From -100 RPM to -1000 RPM
        rotate_motor(left_motor, speed)
        rotate_motor(right_motor, speed)
        print(f"Rotating both motors in reverse at {speed} RPM.")
        time.sleep(5)  # Rotate for 5 seconds at each speed

    # Stop both motors
    stop_motor(left_motor)
    stop_motor(right_motor)
    print("Stopped both motors.")

except Exception as e:
    print("Error:", e)

finally:
    # Ensure motors are stopped before exiting
    stop_motor(left_motor)
    stop_motor(right_motor)

 '''
