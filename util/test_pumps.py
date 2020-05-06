#!/usr/bin/env python

import time
import json

import RPi.GPIO as GPIO


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Read pump configuration
    filename = "../bartender/pump_config.json"
    with open(filename, 'r') as f:
        data = json.load(f)

    # Run each pump for a certain amount of time
    wait = 1
    for pump in data.keys():
        GPIO.setup(data[pump]['pin'], GPIO.OUT, initial=GPIO.HIGH)
        pin = data[pump]['pin']
        print("Testing {} [pin {}] for [{}] second(s)".format(data[pump]['name'], pin, wait))
        GPIO.output(pin, GPIO.LOW)
        time.sleep(wait)
        GPIO.output(pin, GPIO.HIGH)


if __name__ == "__main__":
    main()
