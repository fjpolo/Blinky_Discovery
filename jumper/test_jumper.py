#!/usr/bin/python2
from jumper.vlab import Vlab

# set up the device simulation
v = Vlab(working_directory=".", print_uart=True, platform="nrf52832")
v.load("blinky.bin")

def pins_listener(pin_number, pin_level):
    print("pin_number:", pin_number, "  pin_level:", pin_level)

v.run_for_ms(1000)
v.on_pin_level_event(pins_listener)
print('ran for one second')

v.run_for_us(1000000)
print('ran for one second')

v.run_for_ns(1000000000)
print('ran for one second')

v.stop()

print('Got here, so that means the test result should be OK')