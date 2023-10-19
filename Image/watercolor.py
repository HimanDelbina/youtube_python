import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('1.png')
new_image = cv2.resize(image, (1000,1000))
plt.figure(figsize = [10, 10])

image_resized = cv2.resize(new_image, None, fx=0.9, fy=0.9)
image_cleared = cv2.medianBlur(image_resized, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)
image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)
for i in range(2):
    image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

for i in range(3):
    image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)
gaussian_mask= cv2.GaussianBlur(image_filtered, (7,7), 2)
image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)   


# cv2.imshow('gaussian_mask',gaussian_mask)
cv2.imshow('original_image',new_image)
cv2.imshow('image_sharp',image_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()