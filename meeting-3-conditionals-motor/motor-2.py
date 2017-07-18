#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *


m = LargeMotor('outC')

def spinWheel(speed):
	m.run_to_rel_pos(position_sp=360,speed_sp=speed,stop_action="hold")

Sound.speak('Spin the wheel once').wait()
spinWheel(900)

Sound.speak('Spin the wheel twice').wait()
spinWheel(500)

Sound.speak('Spin the wheel thrice').wait()
spinWheel(100)

