# Importing required libraries
import RPi.GPIO as GPIO
import time

# defininf traffic Light function
def trafficLight(LED_RED, LED_YELLOW, LED_GREEN, timer, previousLed):
    '''
    Input Parameter: LED_RED - Red Light Pin Number for lane to allow traffic
                     LED_YELLOW - Yellow Light Pin Number for lane to allow traffic
                     LED_GREEN - Green Light Pin Number for lane to allow traffic
                     timer - traffic density timer
                     previousLed - Last allowed Len's LED pin number list
    Return: list containing traffic light of lane that was allowed
            to go last time.
    Purpose: to regulate traffic lights of different lanes.
    '''

    # for no change in traffic state
    if previousLed == [LED_RED, LED_YELLOW, LED_GREEN]:
        return previousLed

    # for change in traffic state
    else:
        # assigning previous LED Pin Numbers from array to variables
        EX_LED_RED = previousLed[0]
        EX_LED_YELLOW = previousLed[1]
        EX_LED_GREEN = previousLed[2]

        # flashing Green LED of lane that is going to be closed
        print("Changing the traffic light")
        print("Green LED is flashing!")
        GPIO.output(EX_LED_GREEN, 0)
        time.sleep(0.5) # pause for 500 milliseconds
        GPIO.output(EX_LED_GREEN, 1)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 0)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 1)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 0)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 1)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 0)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 1)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 0)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 1)
        time.sleep(0.5)
        GPIO.output(EX_LED_GREEN, 0)

        # Turning Yellow LED of both lanes for 5 seconds
        GPIO.output(EX_LED_YELLOW, 1)
        GPIO.output(LED_YELLOW, 1)
        print("Yellow LED is ON!")
        time.sleep(5) # pause for 5 seconds
        GPIO.output(EX_LED_YELLOW, 0)
        GPIO.output(LED_YELLOW, 0)

        # Turning on Red LED for lane that is going to be closed
        GPIO.output(EX_LED_RED, 1)
        print("Red LED is ON!")

        # Turning off Red LED for lane that is going to be opened
        GPIO.output(LED_RED, 0)

        # Turning on Green LED for lane that is going to be opened
        GPIO.output(LED_GREEN, 1)
        print("Green LED is ON!")

        # pausing for certain seconds as defined by traffic density
        time.sleep(timer)

        # adding current LEDs to previous LEDs list
        previousLight = [LED_RED, LED_YELLOW, LED_GREEN]

        # retuning previous LEDs
        return previousLight