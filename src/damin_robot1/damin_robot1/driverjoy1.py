import minimalmodbus
import time
import pygame

# Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Serial port parameters
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

# Initialize pygame joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Function to rotate both motors based on joystick input
def rotate_motors(target_velocity):
    left_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable left motor
    right_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable right motor

    left_motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity for left motor
    right_motor.write_register(0x2089, target_velocity, functioncode=6)  # Set target velocity for right motor

def stop_motors():
    left_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop left motor
    right_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop right motor

try:
    while True:
        pygame.event.get()
        # Read joystick axes values
        left_right_axis = joystick.get_axis(0)
        up_down_axis = joystick.get_axis(1)

        # Scale joystick values to motor velocity range (-100 to 100)
        target_velocity = int(left_right_axis * 100)
        
        # Control the motors based on joystick input
        rotate_motors(target_velocity)

        # Get the state of all buttons
        num_buttons = joystick.get_numbuttons()
        pressed_buttons = [button for button in range(num_buttons) if joystick.get_button(button)]

        # Print the state of pressed buttons
        print("Pressed buttons:", pressed_buttons)

        # Sleep for a short time to control loop frequency
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    stop_motors()
    pygame.quit()



""" 
import minimalmodbus
import time
import pygame

# Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Serial port parameters
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

# Initialize pygame joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Function to rotate both motors based on joystick input
def rotate_motors(target_velocity):
    left_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable left motor
    right_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable right motor

    left_motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity for left motor
    right_motor.write_register(0x2089, target_velocity, functioncode=6)  # Set target velocity for right motor

def stop_motors():
    left_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop left motor
    right_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop right motor

try:
    while True:
        pygame.event.get()
        # Read joystick axes values
        left_right_axis = joystick.get_axis(0)
        up_down_axis = joystick.get_axis(1)

        # Scale joystick values to motor velocity range (-100 to 100)
        target_velocity = int(left_right_axis * 100)
        
        # Control the motors based on joystick input
        rotate_motors(target_velocity)

        # Get the state of all buttons
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

        # Print the state of all buttons
        print("Pressed buttons:", [i for i, button in enumerate(buttons) if button])

        # Sleep for a short time to control loop frequency
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    stop_motors()
    pygame.quit()

############################

import minimalmodbus
import time
import pygame

# Modbus RTU slave addresses for left and right motors
LEFT_MOTOR_ADDRESS = 1
RIGHT_MOTOR_ADDRESS = 2

# Serial port parameters
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

# Initialize pygame joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Function to rotate both motors based on joystick input
def rotate_motors(target_velocity):
    left_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable left motor
    right_motor.write_register(0x200E, 0x08, functioncode=6)  # Enable right motor

    left_motor.write_register(0x2088, target_velocity, functioncode=6)  # Set target velocity for left motor
    right_motor.write_register(0x2089, target_velocity, functioncode=6)  # Set target velocity for right motor

def stop_motors():
    left_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop left motor
    right_motor.write_register(0x200E, 0x07, functioncode=6)  # Stop right motor

try:
    while True:
        pygame.event.get()
        # Read joystick axes values
        left_right_axis = joystick.get_axis(0)
        up_down_axis = joystick.get_axis(1)

        # Scale joystick values to motor velocity range (-100 to 100)
        target_velocity = int(left_right_axis * 100)
        
        # Control the motors based on joystick input
        rotate_motors(target_velocity)

        # Sleep for a short time to control loop frequency
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    stop_motors()
    pygame.quit()
"""