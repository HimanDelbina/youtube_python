import cv2
import numpy as np

# Load the input image
input_image_path = '1.png'
input_image = cv2.imread(input_image_path)
input_image = cv2.resize(input_image, (1000, 1000))

# Apply color quantization to reduce the number of colors
num_colors = 8
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, palette = cv2.kmeans(np.float32(input_image).reshape(-1, 3), num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
palette = np.uint8(palette)

# Create a blank output image of the same size as the input image
output_image = np.zeros_like(input_image)

# Replace each pixel with the corresponding color from the palette
for i in range(len(input_image)):
    for j in range(len(input_image[i])):
        pixel_label = labels[i * len(input_image[i]) + j]
        output_image[i, j] = palette[pixel_label]

# Apply additional image manipulation if desired (e.g., contrast adjustment, edge detection)

# Display the input and output images
cv2.imshow('Input Image', input_image)
cv2.imshow('Pop Art Filter', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()