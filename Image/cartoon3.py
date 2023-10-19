from cartooner import cartoonize
import cv2
import os
import time

input_file = '1.png'
image = cv2.imread(input_file)
image = cv2.resize(image, (1000, 1000))
output = cartoonize(image)
cv2.imshow('Cartoon Effect', output)
cv2.waitKey(0)
cv2.destroyAllWindows()