"""
Feature matching
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

if  __name__ == "__main__":
    image_1 = cv2.imread('opencv-feature-matching-image.jpg', 0)
    image_2 = cv2.imread('opencv-feature-matching-template.jpg', 0)

    orb = cv2.ORB_create()

    kp1, dist1 = orb.detectAndCompute(image_1, None)
    kp2, dist2 = orb.detectAndCompute(image_2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    match = bf.match(dist1, dist2)
    match = sorted(match, key= lambda x:x.distance)

    image_3 = cv2.drawMatches(image_1, kp1, image_2, kp2, match[:10], None, flags=2)
    plt.imshow(image_3)
    plt.show()

