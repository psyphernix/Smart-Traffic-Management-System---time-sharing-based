#!/usr/bin/env python3

# Importing required libraries
import RPi.GPIO as GPIO
import time
from ultrasonic import state
from compare import stateComparision
from camera import vehicleCounting

# Setting GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setting GPIO warnings to False
GPIO.setwarnings(False)

# Assigning GPIO Pin Number
# Ultrasonic Sensor 1
US1_TRIGGER = 21
US1_ECHO = 26

# Ultrasonic Sensor 2
US2_TRIGGER = 20
US2_ECHO = 19

# Ultrasonic Sensor 3
US3_TRIGGER = 16
US3_ECHO = 13

# Ultrasonic Sensor 4
US4_TRIGGER = 23
US4_ECHO = 6

# Ultrasonic Sensor 5
US5_TRIGGER = 25
US5_ECHO = 18

# Ultrasonic Sensor 6
US6_TRIGGER = 24
US6_ECHO = 12

# TrafficLights for L1
L1_LED_RED = 15
L1_LED_YELLOW = 4
L1_LED_GREEN = 7

# TrafficLights for L2
L2_LED_RED = 10
L2_LED_YELLOW = 9
L2_LED_GREEN = 5

# TrafficLights for L3
L3_LED_RED = 17
L3_LED_YELLOW = 27
L3_LED_GREEN = 22

# Setting GPIO Pin mode for either in or out
# Ultrasonic Sensor 1
GPIO.setup(US1_TRIGGER, GPIO.OUT)
GPIO.setup(US1_ECHO, GPIO.IN)

# Ultrasonic Sensor 2
GPIO.setup(US2_TRIGGER, GPIO.OUT)
GPIO.setup(US2_ECHO, GPIO.IN)

# Ultrasonic Sensor 3
GPIO.setup(US3_TRIGGER, GPIO.OUT)
GPIO.setup(US3_ECHO, GPIO.IN)

# Ultrasonic Sensor 4
GPIO.setup(US4_TRIGGER, GPIO.OUT)
GPIO.setup(US4_ECHO, GPIO.IN)

# Ultrasonic Sensor 5
GPIO.setup(US5_TRIGGER, GPIO.OUT)
GPIO.setup(US5_ECHO, GPIO.IN)

# Ultrasonic Sensor 6
GPIO.setup(US6_TRIGGER, GPIO.OUT)
GPIO.setup(US6_ECHO, GPIO.IN)

# TrafficLights for L1
GPIO.setup(L1_LED_RED, GPIO.OUT)
GPIO.setup(L1_LED_YELLOW, GPIO.OUT)
GPIO.setup(L1_LED_GREEN, GPIO.OUT)

# TrafficLights for L2
GPIO.setup(L2_LED_RED, GPIO.OUT)
GPIO.setup(L2_LED_YELLOW, GPIO.OUT)
GPIO.setup(L2_LED_GREEN, GPIO.OUT)

# TrafficLights for L3
GPIO.setup(L3_LED_RED, GPIO.OUT)
GPIO.setup(L3_LED_YELLOW, GPIO.OUT)
GPIO.setup(L3_LED_GREEN, GPIO.OUT)

# Setting initial GPIO output for LEDs
# TrafficLights for L1
GPIO.output(L1_LED_RED, 0)
GPIO.output(L1_LED_YELLOW, 0)
GPIO.output(L1_LED_GREEN, 1)

# TrafficLights for L2
GPIO.output(L2_LED_RED, 1)
GPIO.output(L2_LED_YELLOW, 0)
GPIO.output(L2_LED_GREEN, 0)

# TrafficLights for L3
GPIO.output(L3_LED_RED, 1)
GPIO.output(L3_LED_YELLOW, 0)
GPIO.output(L3_LED_GREEN, 0)

# defining main function
def main():
    '''
    Input Parameter: None
    Return: None
    Purpose: Main function to start program by calling modules.
    '''

    # Assigning initial lane counter value
    counterL1 = 1
    counterL2 = 0
    counterL3 = 0
    
    # Assigning initial previous state of LEDs to a list
    previousLED = [L1_LED_RED, L1_LED_YELLOW, L1_LED_GREEN]

    # Creating Try Except statement
    try:
        # Run program until user interruption
        while True:
            samaya = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) # current system time
            print("Time: ", samaya)
            print("Lane 1 count: ", counterL1)
            print("Lane 2 count: ", counterL2)
            print("Lane 3 count: ", counterL3)
            print("Started taking lane data.....")
            #calling state function and assigning return value to a variable status
            status = state(US1_TRIGGER, US1_ECHO, US2_TRIGGER, US2_ECHO, US3_TRIGGER, US3_ECHO, US4_TRIGGER, US4_ECHO, US5_TRIGGER, US5_ECHO, US6_TRIGGER, US6_ECHO)
            vehicleNumber = vehicleCounting()
            print("Lane data taking completed!")
            print("Status : ", status, " , ", vehicleNumber)
            #calling state comaparision function
            (previousLED, counterL1, counterL2, counterL3) = stateComparision(status, vehicleNumber, previousLED, L1_LED_RED, L1_LED_YELLOW, L1_LED_GREEN, L2_LED_RED, L2_LED_YELLOW, L2_LED_GREEN, L3_LED_RED, L3_LED_YELLOW, L3_LED_GREEN, counterL1, counterL2, counterL3)

    # Except statement to quit program on Keyboard Interruption by user
    except KeyboardInterrupt:
        GPIO.cleanup()

# calling main function
if __name__=='__main__':
    main()