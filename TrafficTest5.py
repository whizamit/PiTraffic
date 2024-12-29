#!/usr/bin/python

# Test code for PiTraffic running on Raspberry Pi 5
# Developed by: 
# Author: Amit
# Project: PiTraffic
# Python: 
 
import PiTraffic5
import time

SouthRed = PiTraffic5.Traffic("SOUTH", "RED")
SouthYellow = PiTraffic5.Traffic("SOUTH", "YELLOW")
SouthGreen = PiTraffic5.Traffic("SOUTH", "GREEN")

EastRed = PiTraffic5.Traffic("EAST", "RED")
EastYellow = PiTraffic5.Traffic("EAST", "YELLOW")
EastGreen = PiTraffic5.Traffic("EAST", "GREEN")

NorthRed = PiTraffic5.Traffic("NORTH", "RED")
NorthYellow = PiTraffic5.Traffic("NORTH", "YELLOW")
NorthGreen = PiTraffic5.Traffic("NORTH", "GREEN")

WestRed = PiTraffic5.Traffic("WEST", "RED")
WestYellow = PiTraffic5.Traffic("WEST", "YELLOW")
WestGreen = PiTraffic5.Traffic("WEST", "GREEN")

Buzz = PiTraffic5.Buzzer()

# All direction RED LED ON
def AllRed():
    SouthRed.on()
    EastRed.on()
    NorthRed.on()
    WestRed.on()

AllRed()

try:
    while True:
        Buzz.on()
        time.sleep(0.2)
        Buzz.off()

        EastRed.off()
        EastYellow.on()
        time.sleep(1)
        EastYellow.off()
        EastGreen.on()
        time.sleep(2)
        EastGreen.off()
        EastRed.on()
        time.sleep(1)

        WestRed.off()
        WestYellow.on()
        time.sleep(1)
        WestYellow.off()
        WestGreen.on()
        time.sleep(2)
        WestGreen.off()
        WestRed.on()
        time.sleep(1)

        NorthRed.off()
        NorthYellow.on()
        time.sleep(1)
        NorthYellow.off()
        NorthGreen.on()
        time.sleep(2)
        NorthGreen.off()
        NorthRed.on()
        time.sleep(1)

        SouthRed.off()
        SouthYellow.on()
        time.sleep(1)
        SouthYellow.off()
        SouthGreen.on()
        time.sleep(2)
        SouthGreen.off()
        SouthRed.on()
        time.sleep(1)

except KeyboardInterrupt:
    # No need to call PiTraffic5.closeGPIO() because gpiozero handles cleanup automatically
    pass
