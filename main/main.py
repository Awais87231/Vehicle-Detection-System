#importing the prerequisite libraries
import cv2
import numpy as nm
import os
import datetime
import time
import webbrowser

#validation fields
min_Width = 111
min_Height = 111

#loading the video feed 
frameCapture = cv2.VideoCapture('sourcevid.mp4')


if not frameCapture.isOpened():
    print("Error: Could not open video file.")
