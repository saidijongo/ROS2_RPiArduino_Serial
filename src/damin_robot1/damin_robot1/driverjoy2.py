import minimalmodbus
import time

# Define motor driver address
MOTOR_DRIVER_ADDRESS = 1

# Define motor registers
LEFT_MOTOR_REGISTER = 0x2088
RIGHT_MOTOR_REGISTER = 0x2089
STOP_REGISTER = 0x2031

# Define function codes
ASYNCHRONOUS_VELOCITY_CONTROL = 0x06
SYNCHRONOUS_VELOCITY_CONTROL = 0x10

# Define speeds
SPEED_100_RPM = 0x64
SPEED_NEGATIVE_100_RPM = -0x64

# Define error code
ERROR_CODE = 0x03CB

# Define RS485 port
PORT = "/dev/ttyUSB0"  # Change this to match your setup

# Initialize minimalmodbus
instrument = minimalmodbus.Instrument(PORT, MOTOR_DRIVER_ADDRESS)


def send_command(register, data):
    """
    Send a command to the motor driver.

    :param register: Motor register
    :param data: Data to be sent
    """
    instrument.write_register(register, data, functioncode=ASYNCHRONOUS_VELOCITY_CONTROL, signed=True)


def rotate_motor(motor, direction, speed):
    """
    Rotate the motor in a given direction at a specified speed.

    :param motor: 'left' or 'right'
    :param direction: 'CW' or 'CCW'
    :param speed: Speed in RPM
    """
    register = LEFT_MOTOR_REGISTER if motor == 'left' else RIGHT_MOTOR_REGISTER
    speed_data = SPEED_100_RPM if speed >= 0 else SPEED_NEGATIVE_100_RPM
    direction_data = 0x00 if direction == 'CW' else 0xFF

    # Set motor speed and direction
    send_command(register, speed_data)

    # Wait for motor to stabilize
    time.sleep(1)

    # Stop the motor
    send_command(STOP_REGISTER, ERROR_CODE)


# Example usage
rotate_motor('left', 'CW', 100)
rotate_motor('right', 'CCW', 50)
