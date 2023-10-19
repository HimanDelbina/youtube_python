import cv2
import numpy as np

def convert_to_cartoon(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    blurred = cv2.medianBlur(gray, 5)

    # Perform edge detection
    edges = cv2.Laplacian(blurred, cv2.CV_8U, ksize=5)
    _, thresholded = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    # Apply bilateral filter for cartoon effect
    num_iterations = 7  # Adjust the number of iterations for desired effect
    for _ in range(num_iterations):
        filtered = cv2.bilateralFilter(image, d=9, sigmaColor=9, sigmaSpace=7)

    # Combine the filtered image with the thresholded edges
    cartoon = cv2.bitwise_and(filtered, filtered, mask=thresholded)

    # Display the original image and the cartoon effect
    # cv2.imshow('Original Image', image)
    cv2.imshow('Cartoon Effect', cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
convert_to_cartoon(input_image_path)