#!/usr/bin/env python

import time
import datetime
from Adafruit_7Segment import SevenSegment
from Adafruit_LEDBackpack import LEDBackpack
import signal
import sys

segment = SevenSegment(address=0x70)
seven = LEDBackpack(address=0x70)

# Kinda pack-rat-ish.. these are crumbs I'd like to implement
seven.setBrightness(15)

def exit_gracefully(signum, frame):
    # let's restore the original signal handlers
    signal.signal(signal.SIGTERM, original_sigterm)
    signal.signal(signal.SIGINT, original_sigint)
    signal.signal(signal.SIGHUP, original_sighup)

    # clean up gracefully here. bail when done.
    seven.clear()
    sys.exit(0)

    #just in case we do something during cleanup that means we *shouldn't" exit, we want our handler to stay intact.
    signal.signal(signal.SIGTERM, exit_gracefully)
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGHUP, exit_gracefully)

def run_this():
    # Continually update the time on a 4 char, 7-segment display
    while(True):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        # Set hours
        segment.writeDigit(0, int(hour / 10))     # Tens
        segment.writeDigit(1, hour % 10)          # Ones
        # Set minutes
        segment.writeDigit(3, int(minute / 10))   # Tens
        segment.writeDigit(4, minute % 10)        # Ones
        # Toggle colon
        segment.setColon(second % 2)              # Toggle colon at 1Hz
        # Wait one second
        time.sleep(1)

if __name__ == '__main__':
    # store the original SIGTERM
    original_sigterm = signal.getsignal(signal.SIGTERM)
    original_sigint = signal.getsignal(signal.SIGINT)
    original_sighup = signal.getsignal(signal.SIGHUP)
    signal.signal(signal.SIGTERM, exit_gracefully)
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGHUP, exit_gracefully)
    run_this()


