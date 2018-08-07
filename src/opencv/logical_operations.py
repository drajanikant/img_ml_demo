"""
Titile: Image logicel operations
"""
# Import statements
import cv2
import numpy as nu

# loading the images
image_1 = cv2.imread('img1.jpg')
image_2 = cv2.imread('img2.jpg')
image_3 = cv2.imread('img3.jpg')

# Normal Addition operation 
# add = image_1 + image_2  

# OpenCV Arithmatic operations
# This operation adds the actual pixel values if value greter than 255 it consider as 255
# add = cv2.add(image_1, image_2)

# Weightd images
# weighted = cv2.addWeighted(image_1, 0.6, image_2, 0.4, 0)

# cv2.imshow('weighted of images : ', weighted)

# getting the shapes of images
rows, columns, channels = image_3.shape

# Creating region in images
roi = image_1[0:rows, 0:columns]

# Converting the images into grayscale
img2gray = cv2.cvtColor(image_3, cv2.COLOR_BGR2GRAY)

# Creating the thrushold of image
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# writing the threshold mask in screen
cv2.imshow('Mask images : ', mask)

# Creating inverse of mask
inv_mask = cv2.bitwise_not(mask)

# writing the inverse mask in screen
cv2.imshow('Inverse mask : ', inv_mask)

# gettting the background color of the image1
img1_bg = cv2.bitwise_and(roi, roi, mask=inv_mask)

# writing the gettting the background color in screen
cv2.imshow('gettting the background color : ', img1_bg)

# Getting the foreground color of in image 3
img3_fg = cv2.bitwise_and(image_3, image_3, mask= mask)

# writing the foreground color of in image 3 in screen
cv2.imshow('foreground color of in image 3 : ', img3_fg)

# addition of image 1 and 3
dist = cv2.add(img1_bg, img3_fg)

# writing the addition of image 1 and 3 in screen
cv2.imshow('addition of image 1 and 3 : ', dist)

# Adding the new distribution in the image 1
image_1[0:rows, 0:columns] = dist

# writing new distribution in the image 1 in screen
cv2.imshow('Adding the new distribution in the image 1 : ', image_1)


cv2.waitKey(0)
cv2.destroyAllWindows()
