#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

name = "Elizabeth"
Sound.speak('Hello '+name+', I am your robot').wait()

