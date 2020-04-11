#!/usr/bin/python2
from jumper.vlab import Vlab
import sys

def pins_listener(pin_number, pin_level):
    print("pin_number:", pin_number, "  pin_level:", pin_level)


# set up the device simulation
v = Vlab(working_directory=".", platform = "stm32f407")
print("Platform: STM32F407")
v.load("blinky.bin")
print("blinky.bin loaded!")

v.run_for_ms(1000)
print("\n\r")
v.on_pin_level_event(pins_listener)
print('ran for one second')

v.run_for_us(1000000)
print('ran for one second')

v.run_for_ns(1000000000)
print('ran for one second')

v.stop()

print('Got here, so that means the test result should be OK')