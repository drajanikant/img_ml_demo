# used for the video processing

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Capturing the video
cap = cv2.VideoCapture(0)

# Saving the video in the xvid form
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))
while True:
    # Reading the image frames form the video
    ref, frame = cap.read()
    
    # Converting the color frame into the grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Showing grayscale output
    cv2.imshow('Gray', gray)

    # Showing the color output
    cv2.imshow('Frame', frame)
    
    # Writing the data into the file
    out.write(frame)

    # Creating the exit scanario
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()