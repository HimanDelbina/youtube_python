import cv2
import numpy as np

def convert_to_cartoon(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))

    # Apply bilateral filtering to reduce noise and smoothen the image
    filtered = cv2.bilateralFilter(image, 9, 75, 75)

    # Convert the filtered image to grayscale
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to create a binary image
    _, edges = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Apply a median blur to further simplify the image
    blurred = cv2.medianBlur(edges, 5)

    # Create a color version of the image for overlay
    color = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Set the saturation of the color image to a fixed value
    color[:, :, 1] = 100

    # Convert the color image back to BGR format
    color = cv2.cvtColor(color, cv2.COLOR_HSV2BGR)

    # Apply the cartoon effect by combining the color overlay and the simplified image
    cartoon = cv2.bitwise_and(color, color, mask=blurred)
    cv2.imshow('Cartoon Effect', cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
convert_to_cartoon(input_image_path)