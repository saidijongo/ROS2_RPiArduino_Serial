import tkinter as tk
import multiprocessing
#from motor_control import MotorControl
import gamepadMotor

class RobotControlGUI:
    def __init__(self, motor_control):
        self.root = tk.Tk()
        self.root.title("Robot Control")
        self.motor_control = motor_control

        #buttons for controlling the robot
        self.btn_forward = tk.Button(self.root, text="Forward", command=self.move_forward)
        self.btn_backward = tk.Button(self.root, text="Backward", command=self.move_backward)
        self.btn_left = tk.Button(self.root, text="Left", command=self.move_left)
        self.btn_right = tk.Button(self.root, text="Right", command=self.move_right)
        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop)

        # Place buttons on the GUI
        self.btn_forward.grid(row=0, column=1)
        self.btn_backward.grid(row=2, column=1)
        self.btn_left.grid(row=1, column=0)
        self.btn_right.grid(row=1, column=2)
        self.btn_stop.grid(row=1, column=1)

        self.root.mainloop()

    def move_forward(self):
        self.motor_control.move_forward()

    def move_backward(self):
        self.motor_control.move_backward()

    def move_left(self):
        self.motor_control.move_left()

    def move_right(self):
        self.motor_control.move_right()

    def stop(self):
        self.motor_control.stop()

if __name__ == "__main__":
    motor_control = MotorControl()
    gui = RobotControlGUI(motor_control)
