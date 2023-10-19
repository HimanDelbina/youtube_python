import cv2

# Load the input image
input_image_path = '1.png'
input_image = cv2.imread(input_image_path)
input_image = cv2.resize(input_image, (1000, 1000))

# Define the pixel size for the pixelation effect
pixel_size = 7

# Calculate the dimensions of the pixelated blocks
height, width = input_image.shape[:2]
new_height = height // pixel_size
new_width = width // pixel_size

# Resize the image to the new dimensions
resized_image = cv2.resize(input_image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

# Upscale the resized image back to the original size
pixelated_image = cv2.resize(resized_image, (width, height), interpolation=cv2.INTER_NEAREST)

# Display the input and pixelated images
# cv2.imshow('Input Image', input_image)
cv2.imshow('Pixelated Image', pixelated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()