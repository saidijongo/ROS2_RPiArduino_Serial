import pygame
#from motor_control import MotorControl
import gamepadMotor

class GamepadControl:
    def __init__(self, motor_control):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        self.motor_control = motor_control

    def control_robot(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.motor_control.move_forward()
                    elif event.button == 1:
                        self.motor_control.move_backward()
                    elif event.button == 2:
                        self.motor_control.move_left()
                    elif event.button == 3:
                        self.motor_control.move_right()
                    elif event.button == 4:
                        self.motor_control.stop()

if __name__ == "__main__":
    motor_control = MotorControl()
    gamepad_control = GamepadControl(motor_control)
    gamepad_control.control_robot()
