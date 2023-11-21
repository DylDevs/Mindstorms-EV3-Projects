# Project Description
# This project uses the Infared Sensor on the robot to recive inputs from the remote
# Using those inputs it moves the robots wheels in the appropriate direction

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize Motors and Sensors
right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
infrared_sensor = InfraredSensor(Port.S2)

# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()

while True:
    pressed = str(infrared_sensor.keypad())
    if "Button.LEFT_UP" in pressed:
        left_motor.run(1000)
    elif "Button.LEFT_DOWN" in pressed:
        left_motor.run(-1000)
    else:
        left_motor.brake()
    
    if "Button.RIGHT_UP" in pressed:
        right_motor.run(1000)
    elif "Button.RIGHT_DOWN" in pressed:
        right_motor.run(-1000)
    else:
        right_motor.brake()
