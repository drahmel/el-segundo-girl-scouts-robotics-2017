#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *


m = LargeMotor('outC')
Sound.speak('Spin the wheel once').wait()
m.run_to_rel_pos(position_sp=360,speed_sp=900,stop_action="hold")
Sound.speak('Spin the wheel twice').wait()
m.run_to_rel_pos(position_sp=360,speed_sp=900,stop_action="hold")
Sound.speak('Spin the wheel thrice').wait()
m.run_to_rel_pos(position_sp=360,speed_sp=900,stop_action="hold")
