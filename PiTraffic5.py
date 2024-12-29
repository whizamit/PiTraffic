#!/usr/bin/python

# Library for PiTraffic running on Raspberry Pi 5
# Developed by: 
# Author: Amit
# Project: PiTraffic
# Python: 3.11.2

# updated to use gpiozero 
# changed pin numbers to use BCM asd BOARD numdering is not suported

import time
from gpiozero import LED
from gpiozero import Button as GPIOButton

def closeGPIO():
    # gpiozero handles cleanup automatically, so this function can be omitted
    pass

class Buzzer:
    def __init__(self):
        self.pin = 18  # Use BCM 18 for the buzzer (Physical Pin 12)
        self.buzzer = LED(self.pin)  # Use gpiozero LED class for controlling the buzzer
        self.buzzer.off()

    def on(self):
        print("Buzzer - ON")
        self.buzzer.on()

    def off(self):
        print("Buzzer - OFF")
        self.buzzer.off()


class Traffic:
    ''' Class to handle LED's

    Arguments:
    direction =  (i.e. "EAST", "WEST", "NORTH", "SOUTH")
    color = Color of LED
    '''

    # Updated pins to use BCM pin numbers
    traffic_pins = {
        "SOUTH": {'RED': 17, 'YELLOW': 27, "GREEN": 22},
        "WEST": {'RED': 23, 'YELLOW': 24, "GREEN": 25},
        "NORTH": {'RED': 5, 'YELLOW': 6, "GREEN": 13},
        "EAST": {'RED': 16, 'YELLOW': 20, "GREEN": 21}
    }

    def __init__(self, direction, color):
        self.pin = self.traffic_pins[direction][color]
        self.direction = direction
        self.color = color
        self.led = LED(self.pin)  # Use gpiozero LED class for controlling the traffic light

    def on(self):
        print(self.direction + " " + self.color + " - ON")
        self.led.on()

    def off(self):
        print(self.direction + " " + self.color + " - OFF")
        self.led.off()

class Button:
    def __init__(self, pin=4):  # Default to BCM 4 if no pin is specified
        self.pin = pin
        self.button = GPIOButton(self.pin)  # Create gpiozero Button object with the specified pin
        self.Pressed = False

    def press(self):
        if self.button.is_pressed:
            print("Button - Pressed")
            self.Pressed = True