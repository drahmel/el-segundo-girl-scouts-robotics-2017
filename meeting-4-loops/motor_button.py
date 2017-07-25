#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

m = LargeMotor('outC')

button = TouchSensor();

print("Waiting for the button")
while not ts.value():
	m.run_to_rel_pos(position_sp=1,speed_sp=900)
        Leds.set_color(Leds.LEFT, Leds.RED)

print("You hit the button!")
Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)

