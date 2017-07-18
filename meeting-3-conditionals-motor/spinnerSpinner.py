#!/usr/bin/env python3
# so that script can be run from Brickman

from time import sleep
from ev3dev.ev3 import *

m = LargeMotor('outA')
m.run_to_abs_pos(position_sp=120,speed_sp=1000,stop_action="hold")
m.wait_while('running')
sleep(10)
m.run_to_abs_pos(position_sp=20,speed_sp=100,stop_action="hold")
m.wait_while('running')
