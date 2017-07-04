#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

Leds.set_color(Leds.LEFT, Leds.RED)

Sound.tone(1500, 200).wait()

Leds.set_color(Leds.LEFT, Leds.ORANGE)

name = "Josefeen"
message = 'Hello '+name+', I am your robot'
Sound.speak(message).wait()

Leds.set_color(Leds.LEFT, Leds.GREEN)
