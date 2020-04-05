# importing all required libraries
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from picamera import PiCamera
from time import sleep

camerapi = PiCamera() # powerup camera
# defining camera module to take picture of a road
def camera():
    '''
    Input Parameter: None
    Return: None
    Purpose: to take image using raspberry camera and save to local disk
    '''
    
    camerapi.start_preview() # start camera preview
    sleep(5) # stop program processing for 5 seconds to take better picture
    camerapi.capture('image.jpeg') #capture image and save as image.jpeg
    camerapi.stop_preview()  # stop camera preview
    return None # returning nothing
     
# defining object recognition and counting module
def vehicleCounting():
    '''
    Input Parameter: None
    Return: vehicleNumber -  number of vehicles in the road
    Purpose: to detect vehicle and count number
    '''
    
    camera() # taking image
    image = cv2.imread('image.jpeg') # converting image to numpy array using opencv library
    image = image[250:550, 0:1280] # cropping image
    bbox, label, conf = cv.detect_common_objects(image) # detecting common objects using yolov3 trained model and label them
    vehicleNumber = label.count('car')+label.count('truck')+label.count('bus')+label.count('motorcycle') # count common vehicles
    return int(vehicleNumber) # return number of vehicles
    
