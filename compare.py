# importing all required libraries
from led import trafficLight

# defining a function for state comparision
def stateComparision(state, stateCam, previousLED, r1, y1, g1, r2, y2, g2, r3, y3, g3, counterL1, counterL2, counterL3):
    '''
    Input Parameter: state - Traffic State in different lanes
                     previousLED - last traffic light state
                     r1, y1, g1 - Lane 1 Traffic Lights
                     r2, y2, g2 - Lane 2 Traffic Lights 
                     r3, y3, g3 - Lane 3 Traffic Lights
                     counterL1 - Lane 1 counter
                     counterL2 - Lane 2 counter
                     counterL3 - Lane 3 counter
    Return: data from Traffic Light Module, counter of different lanes
    Purpose: to compare all possible valid states of traffic to regulate traffic light.
    '''
    timer1 = 5 # timer for low density traffic
    timer2 = 45 # timer for high density traffic
    
    # Comparing all possible valid states of traffic
    # high traffic in lane 3 from camera and ultrasonic
    if stateCam >= 5 and (state[2:4] == [1,1] or state[2:4] == [0,1]):
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3
    
    # no traffic in all lanes
    elif state == [0,0,0,0,0,0]:
        if (counterL1 <= counterL2) and (counterL1 <= counterL3):
            counterL1 = 1
            return trafficLight(r1, y1, g1, timer1,previousLED), counterL1, counterL2, counterL3

        elif counterL2 <= counterL3:
            counterL2 = 1
            return trafficLight(r2, y2, g2, timer1, previousLED), counterL1, counterL2, counterL3

        else:
            counterL1, counterL2, counterL3 = 0, 0, 0
            return trafficLight(r3, y3, g3, timer1, previousLED), counterL1, counterL2, counterL3

    # low traffic in lane 1
    elif state == [0,0,0,0,0,1]:
        return trafficLight(r1, y1, g1, timer1, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 1
    elif state == [0,0,0,0,1,1]:
        return trafficLight(r1, y1, g1, timer2, previousLED), counterL1, counterL2, counterL3

    # low traffic in lane 3
    elif state == [0,0,0,1,0,0]:
        return trafficLight(r3, y3, g3, timer1, previousLED), counterL1, counterL2, counterL3

    # low traffic in both lane 1 and lane 3
    elif state == [0,0,0,1,0,1]:
        return trafficLight(r3, y3, g3, timer1, previousLED), counterL1, counterL2, counterL3            
    
    # high traffic in lane 1 and low in lane 3
    elif state == [0,0,0,1,1,1]:
        return trafficLight(r1, y1, g1, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 3
    elif state == [0,0,1,1,0,0]:
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # low traffic in lane 1 and high in lane 3
    elif state == [0,0,1,1,0,1]:
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in both lane 1 and lane 3
    elif state == [0,0,1,1,1,1]:
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # low traffic in lane 2
    elif state == [0,1,0,0,0,0]:
        return trafficLight(r2, y2, g2, timer1, previousLED), counterL1, counterL2, counterL3

    # low traffic in both lane 1 and lane 2
    elif state == [0,1,0,0,0,1]:
        return trafficLight(r1, y1, g1, timer1, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 1 and low in 2
    elif state == [0,1,0,0,1,1]:
        return trafficLight(r1, y1, g1, timer2, previousLED), counterL1, counterL2, counterL3

    # low traffic in both lane 2 and lane 3
    elif state == [0,1,0,1,0,0]:
        return trafficLight(r2, y2, g2, timer1, previousLED), counterL1, counterL2, counterL3

    # low traffic in all lanes
    elif state == [0,1,0,1,0,1]:
        if (counterL1 <= counterL2) and (counterL1 <= counterL3):
            counterL1 = 1
            return trafficLight(r1, y1, g1, timer1,previousLED), counterL1, counterL2, counterL3

        elif counterL2 <= counterL3:
            counterL2 = 1
            return trafficLight(r2, y2, g2, timer1, previousLED), counterL1, counterL2, counterL3

        else:
            counterL1, counterL2, counterL3 = 0, 0, 0
            return trafficLight(r3, y3, g3, timer1, previousLED), counterL1, counterL2, counterL3

    # low traffic in both lane 2 and 3 and high in lane 1
    elif state == [0,1,0,1,1,1]:
        return trafficLight(r1, y1, g1, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 3 and low in lane 2
    elif state == [0,1,1,1,0,0]:
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 3 and low in both 1 and 2
    elif state == [0,1,1,1,0,1]:
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in both lane 1 and land 3 and low in 2
    elif state == [0,1,1,1,1,1]:
        return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 2
    elif state == [1,1,0,0,0,0]:
        return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 2 and low in lane 1
    elif state == [1,1,0,0,0,1]:
        return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in both lane 1 and lane 2
    elif state == [1,1,0,0,1,1]:
        return trafficLight(r1, y1, g1, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 2 and low in lane 3    
    elif state == [1,1,0,1,0,0]:
        return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in lane 2 and low in both lane 1 and lane 3
    elif state == [1,1,0,1,0,1]:
        return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in both lane 1 and lane 2 and low in lane 3
    elif state == [1,1,0,1,1,1]:
        return trafficLight(r1, y1, g1, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in both lane 2 and lane 3
    elif state == [1,1,1,1,0,0]:
        return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in both lane 2 and lane 3 and low in lane 1
    elif state == [1,1,1,1,0,1]:
        return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

    # high traffic in all lanes
    elif state == [1,1,1,1,1,1]:
        if (counterL1 <= counterL2) and (counterL1 <= counterL3):
            counterL1 = 1
            return trafficLight(r1, y1, g1, timer2,previousLED), counterL1, counterL2, counterL3

        elif counterL2 <= counterL3:
            counterL2 = 1
            return trafficLight(r2, y2, g2, timer2, previousLED), counterL1, counterL2, counterL3

        else:
            counterL1, counterL2, counterL3 = 0, 0, 0
            return trafficLight(r3, y3, g3, timer2, previousLED), counterL1, counterL2, counterL3

    # to handle invalid traffic states
    else:
        # check if camera detected any vehicle in lane 3
        if stateCam > 0 and stateCam <= 2:
            return trafficLight(r3, y3, g3, timer1, previousLED), counterL1, counterL2, counterL3
        
        elif (counterL1 <= counterL2) and (counterL1 <= counterL3):
            counterL1 = 1
            return trafficLight(r1, y1, g1, timer1,previousLED), counterL1, counterL2, counterL3

        elif counterL2 <= counterL3:
            counterL2 = 1
            return trafficLight(r2, y2, g2, timer1, previousLED), counterL1, counterL2, counterL3

        else:
            counterL1, counterL2, counterL3 = 0, 0, 0
            return trafficLight(r3, y3, g3, timer1, previousLED), counterL1, counterL2, counterL3
