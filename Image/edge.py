import cv2
import numpy as np

def convert_to_cartoon(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter for noise reduction and smoothing
    filtered = cv2.bilateralFilter(image, 9, 75, 75)

    # Perform edge detection using Canny edge detector
    edges = cv2.Canny(gray, 100, 200)

    # Invert the edges to create a mask
    edges_inv = cv2.bitwise_not(edges)

    # Use the edges mask to extract the cartoon-like image
    cartoon = cv2.bitwise_and(filtered, filtered, mask=edges_inv)

    # Display the original image and the cartoon effect
    # cv2.imshow('Original Image', image)
    cv2.imshow('Cartoon Effect', cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
convert_to_cartoon(input_image_path)