#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *


button = TouchSensor();

print("Waiting for the button")
while not ts.value():
        Leds.set_color(Leds.LEFT, Leds.RED)

print("You hit the button!")
Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)

