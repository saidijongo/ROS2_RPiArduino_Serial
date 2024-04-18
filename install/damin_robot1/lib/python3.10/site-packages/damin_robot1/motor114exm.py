''' 
###eg.1 #####
import minimalmodbus

def read_holding_registers():
    slave_address = 1
    start_address = 0x0145
    number_of_points = 1

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_address)
    read_data = instrument.read_registers(start_address, number_of_points)
    
    return read_data

read_data = read_holding_registers()
print("Read data:", read_data)
'''

###eg.2#####
''' 
import minimalmodbus

def servo_on():
    servo_on_addr = 0x200E
    servo_on_command_data = 0x08
    slave_id = 1

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_id)
    instrument.write_register(servo_on_addr, servo_on_command_data)

def servo_off():
    servo_on_addr = 0x200E
    servo_on_command_data = 0x07
    slave_id = 1

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_id)
    instrument.write_register(servo_on_addr, servo_on_command_data)

servo_on()
# Wait or do some operations
servo_off()
'''

###eg.3 ####
'''
import minimalmodbus

def write_single_register():
    slave_address = 1
    register_address = 0x600A
    value = 0x0004

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_address)
    instrument.write_register(register_address, value)

write_single_register()

'''

###eg.4 ####
'''
import minimalmodbus

def servo_on():
    servo_on_addr = 0x200E
    servo_on_command_data = 0x08
    slave_id = 1

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_id)
    instrument.write_register(servo_on_addr, servo_on_command_data)

def servo_off():
    servo_on_addr = 0x200E
    servo_on_command_data = 0x07
    slave_id = 1

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_id)
    instrument.write_register(servo_on_addr, servo_on_command_data)

# Usage
servo_on()
# Wait or do some operations
servo_off()

'''

###eg.5 ####
'''
import minimalmodbus

def set_velocity_mode():
    control_mode_addr = 0x200D
    left_motor_velocity_addr = 0x208E
    right_motor_velocity_addr = 0x208F
    control_mode_value = 0x03

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.write_register(control_mode_addr, control_mode_value)
    
    left_motor_velocity = 100
    instrument.write_register(left_motor_velocity_addr, left_motor_velocity)
    
    right_motor_velocity = 100
    instrument.write_register(right_motor_velocity_addr, right_motor_velocity)

set_velocity_mode()

'''

###eg.6 ####

'''
import minimalmodbus

def check_current_velocity():
    slave_id = 1
    read_data = []
    
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_id)
    read_data = instrument.read_registers(0x20AB, 2)
    
    read_left_velocity = read_data[0]
    read_right_velocity = read_data[1]
    
    return read_left_velocity, read_right_velocity

left_velocity, right_velocity = check_current_velocity()
print("Left Velocity:", left_velocity)
print("Right Velocity:", right_velocity)

'''

