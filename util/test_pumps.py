#!/usr/bin/env python

import time
import json

import RPi.GPIO as GPIO


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    filename = "../bartender/pump_config.json"

    # Read pump config and configure each GPIO pin
    with open(filename, 'r') as f:
        data = json.loads(f)

    for pump in data.keys():
        GPIO.setup(data[pump]['pin'], GPIO.OUT, initial=GPIO.HIGH)

    # Run each pump for a certain amount of time
    wait = 1
    for pump in data.keys():
        pin = data[pump]['pin']
        print("Testing {} [pin {}] for [{}] second(s)".format(data[pump]['name'], pin, wait))
        GPIO.output(pin, GPIO.LOW)
        time.sleep(wait)
        GPIO.output(pin, GPIO.HIGH)


if __name__ == "__main__":
    main()
