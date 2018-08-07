"""
Understanding the throusholding of an images using OpenCV
"""

import numpy as np
import cv2

# reading the old book images 
img = cv2.imread('old_book_page.jpeg')

# Showing the original images
cv2.imshow('Original images', img)

# Creating the throushold of an images
retval, threshold = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# Displaying the threshold  values [ Color ]
cv2.imshow('Original images thorshold', threshold)

# Converting the image into grayscale and making thorshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# Displaying the threshold  values [ Color ]
cv2.imshow('Gray scale images thorshold', threshold2)

# Creating gaussion throushold
gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# Displaying the Gaussian threshold  values [ Color ]
cv2.imshow('Gaussian thorshold', gaus)

# Code for holding the output on the screen
cv2.waitKey(0)
cv2.destroyAllWindows()