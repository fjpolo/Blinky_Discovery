#!/usr/bin/python2
from jumper.vlab import Vlab
import sys

# set up the device simulation
v = Vlab(working_directory=".", platform = "stm32f407")
print("Platform: STM32F407")
v.load("blinky.bin")
print("blinky.bin loaded!")

v.run_for_ms(1000)
v.stop()
