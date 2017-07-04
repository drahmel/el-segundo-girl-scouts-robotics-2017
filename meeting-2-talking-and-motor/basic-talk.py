#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

Leds.set_color(Leds.LEFT, Leds.RED)

Sound.tone(1500, 2000).wait()

Leds.set_color(Leds.LEFT, Leds.ORANGE)

name = "Dan"
message = 'Hello '+name+', I am your robot'
Sound.speak(message).wait()

Leds.set_color(Leds.LEFT, Leds.GREEN)
