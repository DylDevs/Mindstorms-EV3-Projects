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
infrared_sensor = InfraredSensor(Port.S2)
Robot = DriveBase(left_motor, right_motor, 275.2, 165)
Robot.settings(straight_speed=1000)

# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()

while True:
    print(infrared_sensor.distance())
    Robot.drive(1000, 0)
    if infrared_sensor.distance() <= 25:
        Robot.straight(-500)
        Robot.turn(900)
