#!/usr/bin/python

# New test code for PiTraffic running on Raspberry Pi 5 that includes LEDs, Buzzer, and Button
# Developed by: 
# Author: Amit
# Project: PiTraffic
# Python: 3.11.2
 
import PiTraffic5
import time

# Initialize the button and buzzer
button = PiTraffic5.Button()
buzzer = PiTraffic5.Buzzer()

# Initialize the traffic lights for all directions
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

# List of directions in order
directions = ["SOUTH", "EAST", "NORTH", "WEST"]

# Function to turn all LEDs on for a specific direction
def turn_leds_on(direction):
    if direction == "SOUTH":
        SouthRed.on()
        SouthYellow.on()
        SouthGreen.on()
    elif direction == "EAST":
        EastRed.on()
        EastYellow.on()
        EastGreen.on()
    elif direction == "NORTH":
        NorthRed.on()
        NorthYellow.on()
        NorthGreen.on()
    elif direction == "WEST":
        WestRed.on()
        WestYellow.on()
        WestGreen.on()

# Function to turn all LEDs off for a specific direction
def turn_leds_off(direction):
    if direction == "SOUTH":
        SouthRed.off()
        SouthYellow.off()
        SouthGreen.off()
    elif direction == "EAST":
        EastRed.off()
        EastYellow.off()
        EastGreen.off()
    elif direction == "NORTH":
        NorthRed.off()
        NorthYellow.off()
        NorthGreen.off()
    elif direction == "WEST":
        WestRed.off()
        WestYellow.off()
        WestGreen.off()

try:
    press_count = 0
    while press_count < 4:  # We want to repeat for 4 directions
        print("Waiting for button press...")
        button.button.wait_for_press()  # Wait for the button press
        
        # Buzzer on for 0.2 seconds
        print("Button pressed, turning buzzer on...")
        buzzer.on()
        time.sleep(0.2)
        buzzer.off()
        print()

        # Turn LEDs on for the next direction
        direction = directions[press_count]
        print(f"Turning on LEDs for {direction} direction...")
        turn_leds_on(direction)
        time.sleep(2)  # Keep LEDs on for 2 seconds

        # Turn LEDs off for the current direction
        print(f"Turning off LEDs for {direction} direction...")
        turn_leds_off(direction)
        print()
        
        press_count += 1  # Move to the next direction

except KeyboardInterrupt:
    print("Test interrupted by user.")
