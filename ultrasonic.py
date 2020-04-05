# Importing required libraries
import RPi.GPIO as GPIO
import time

# defining state function
def state(us1t, us1e, us2t, us2e, us3t, us3e, us4t, us4e, us5t, us5e, us6t, us6e):
    '''
    Input Parameter: us1t - Ultrasonic Sensor 1 Trigger Pin Number
                     us1e - Ultrasonic Sensor 1 Echo Pin Number
                     us2t - Ultrasonic Sensor 2 Trigger Pin Number
                     us2e - Ultrasonic Sensor 2 Echo Pin Number
                     us3t - Ultrasonic Sensor 3 Trigger Pin Number
                     us3e - Ultrasonic Sensor 3 Echo Pin Number
                     us4t - Ultrasonic Sensor 4 Trigger Pin Number
                     us4e - Ultrasonic Sensor 4 Echo Pin Number
                     us5t - Ultrasonic Sensor 5 Trigger Pin Number
                     us5e - Ultrasonic Sensor 5 Echo Pin Number
                     us6t - Ultrasonic Sensor 6 Trigger Pin Number
                     us6e - Ultrasonic Sensor 6 Echo Pin Number
    Return: return value from traffic check by calling it.
    Purpose: to check traffic density in different lanes.
    '''

    # defining distance function
    def distance(TRIGGER, ECHO):
        '''
        Input Parameter: Trigger - Trigger Pin Number
                         Echo - Echo Pin Number
        Return: True or False
        Purpose: To calculate distance of object from ultrasonic sensor in
        centimeters and return True if object is within 10 cm else False
        '''
        # generating pulse serring Trigger to True for 10 microseconds
        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)

        # set start time when echo is low
        while GPIO.input(ECHO) == 0:
            StartTime = time.time()

        # set stop time while echo is high
        while GPIO.input(ECHO) == 1:
            StopTime = time.time()

        # time taken by sound to reach back to sensor
        TimeElapsed = StopTime - StartTime

        # calculating object distance (speed of sound in air - 340 m/s)
        distance = (TimeElapsed * 34000) / 2

        # returning True if object is between 2 cm and 10 cm else False
        return True if distance <= 10 and distance >= 2 else False

    # definfing traffic check function
    def trafficCheck():
        '''
        Input Parameter: None
        Return: Stat - an array containing six value. Each value can be
                either True or False.
        Purpose: To check stopped traffic at the junction. If obstacle is
        dedected continuously for 30 distance calculation, there is considered
        to be a traffic jam.
        Note: Uses distance function
        '''
        # creating arrays for different ultrasonic sensors
        array1 = []
        array2 = []
        array3 = []
        array4 = []
        array5 = []
        array6 = []

        # taking data from each sensor for 15 times
        for i in range(15):
            # taking data from ultrasonic sensor 2
            dist2 = distance(us2t, us2e) # obstacle detection
            array2.append(dist2) # append data to a list
            time.sleep(.170) # pause for 170 milliseconds

            # taking data from ultrasonic sensor 3
            dist3 = distance(us3t, us3e)
            array3.append(dist3)
            time.sleep(.170)
            
            # taking data from ultrasonic sensor 6
            dist6 = distance(us6t, us6e)
            array6.append(dist6)
            time.sleep(.170)

            # taking data from ultrasonic sensor 1
            dist1 = distance(us1t, us1e)
            array1.append(dist1)
            time.sleep(.170)

            # taking data from ultrasonic sensor 4
            dist4 = distance(us4t, us4e)
            array4.append(dist4)
            time.sleep(.170)

            # taking data from ultrasonic sensor 5
            dist5 = distance(us5t, us5e)
            array5.append(dist5)
            time.sleep(.170)

        # creating a list containing traffic state of different lanes
        # all() function takes iterable and returns True if all elements are True
        stat = [all(array1), all(array2), all(array3), all(array4), all(array5), all(array6)]
        return stat

    return trafficCheck()