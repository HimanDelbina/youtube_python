import cv2
import numpy as np

# Load the input image
image_path = '1.png'
input_image = cv2.imread(image_path)
input_image = cv2.resize(input_image, (1000, 1000))

# Convert the image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Apply a median blur to reduce noise
blurred_image = cv2.medianBlur(gray_image, 5)

# Perform edge detection using the Canny edge detector
edges = cv2.Canny(blurred_image, 30, 100)

# Perform adaptive thresholding to obtain a binary image
_, thresholded_image = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY_INV)

# Create a color version of the thresholded image
color_thresholded = cv2.cvtColor(thresholded_image, cv2.COLOR_GRAY2BGR)

# Perform a bilateral filter to smoothen the colors
bilateral_filtered = cv2.bilateralFilter(input_image, 9, 75, 75)

# Combine the color thresholded image with the filtered image using bitwise and
cartoon_image = cv2.bitwise_and(bilateral_filtered, color_thresholded)

# Display the cartoon image
cv2.imshow('Cartoon Image', cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the cartoon image
# output_path = 'output_cartoon_image.jpg'
# cv2.imwrite(output_path, cartoon_image)