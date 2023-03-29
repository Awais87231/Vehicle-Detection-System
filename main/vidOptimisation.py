#reading the video feed
    frameReturn, mainFrame = frameCapture.read()
    greyFrame = cv2.cvtColor(mainFrame, cv2.COLOR_BGR2GRAY) #converting to greyscale as it reduces the model complexity
    blurFrame = cv2.GaussianBlur(greyFrame, (5, 5), 5) #adding a blur frame to increase robustness
    imgSubtract = bgSubtractor.apply(blurFrame) #bgSubtractor function to reduce memory usage
    dilateFrame = cv2.dilate(imgSubtract, nm.ones((5, 5))) #dilating the pixels to increase the size of the said frames, and increase accuracy
    kernelFrame = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) #creating a structuring element of a particular shape
    dilateApply = cv2.morphologyEx(dilateFrame, cv2.MORPH_CLOSE, kernelFrame) #applying the dilate frames
    dilateApply = cv2.morphologyEx(dilateApply, cv2.MORPH_CLOSE, kernelFrame)
    vehicleContour, h = cv2.findContours(dilateApply, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #retrieving the contours in a numpy array
