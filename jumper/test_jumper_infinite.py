#!/usr/bin/python2
from jumper.vlab import Vlab
import sys

# this array holds the four LEDs' visualisation
LEDs=["..","..","..",".."]

def on_pin(number, level):
	#print(number, level)
	# update the state of the simulated LEDs
    if level:
        LEDs[number-60] = "XX"
    else:
        LEDs[number-60] = ".."
    # show them in the terminal
    print "   " + LEDs[0] + "   " + LEDs[1] + "   " + LEDs[2] + "   " + LEDs[3],
    sys.stdout.flush()
    print "\r",

	

# set up the device simulation
v = Vlab(working_directory=".", platform = "stm32f407")
print("Platform: STM32F407")
v.load("blinky.bin")
print("blinky.bin loaded!")

# register the callback which visualises the LEDs
#v.run_for_ms(5000)
v.on_pin_level_event(on_pin)
#print("Ran fo 5 seconds!!")

# run the simulation
v.start()