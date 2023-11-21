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

# Initialize Motors, Sensors, and DriveBase
right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
blade_motor = Motor(Port.C)
infrared_sensor = InfraredSensor(Port.S2)
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S3)
Robot = DriveBase(left_motor, right_motor, 275.2, 165)
Robot.settings(straight_speed=1000)

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