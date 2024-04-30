#include <iostream>
#include <modbus/modbus.h>
#include <unistd.h>

#define MOTOR_DRIVER_ADDRESS 1
#define LEFT_MOTOR_REGISTER 0x2088
#define RIGHT_MOTOR_REGISTER 0x2089
#define STOP_REGISTER 0x2031

#define ASYNCHRONOUS_VELOCITY_CONTROL 0x06
#define SYNCHRONOUS_VELOCITY_CONTROL 0x10

#define SPEED_100_RPM 0x64
#define SPEED_NEGATIVE_100_RPM -0x64

#define ERROR_CODE 0x03CB

int main() {
    // Open Modbus RTU connection
    modbus_t *ctx = modbus_new_rtu("/dev/ttyUSB0", 115200, 'N', 8, 1);
    if (ctx == NULL) {
        std::cerr << "Unable to create Modbus context" << std::endl;
        return 1;
    }

    // Connect to the RS485-to-USB converter
    if (modbus_connect(ctx) == -1) {
        std::cerr << "Modbus connection failed: " << modbus_strerror(errno) << std::endl;
        modbus_free(ctx);
        return 1;
    }

    // Set the slave address for the motor driver
    modbus_set_slave(ctx, MOTOR_DRIVER_ADDRESS);

    // Rotate the left motor clockwise at 100 RPM
    modbus_write_register(ctx, LEFT_MOTOR_REGISTER, SPEED_100_RPM);
    usleep(1000000); // Wait for motor to stabilize
    modbus_write_register(ctx, STOP_REGISTER, ERROR_CODE);

    // Rotate the right motor counterclockwise at 50 RPM
    modbus_write_register(ctx, RIGHT_MOTOR_REGISTER, SPEED_NEGATIVE_100_RPM);
    usleep(1000000); // Wait for motor to stabilize
    modbus_write_register(ctx, STOP_REGISTER, ERROR_CODE);

    // Close Modbus connection
    modbus_close(ctx);
    modbus_free(ctx);

    return 0;
}
