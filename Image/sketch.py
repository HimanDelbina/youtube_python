import cv2
import numpy as np

def convert_to_sketch(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted = cv2.bitwise_not(grayscale)

    # Apply Gaussian blur to smoothen the image
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred)

    # Blend the inverted blurred image with the original grayscale image using the "color dodge" blending mode
    sketch = cv2.divide(grayscale, inverted_blurred, scale=256.0)

    # Display the original image and the sketch
    cv2.imshow('Original Image', image)
    cv2.imshow('Sketch', sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
convert_to_sketch(input_image_path)