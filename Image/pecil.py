import cv2
import numpy as np

def convert_image_to_pencil_art(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    
    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    
    # Blend the grayscale image and the blurred image using the "color dodge" blend mode
    pencil_art = cv2.divide(gray_image, blurred_image, scale=256.0)
    
    return pencil_art

# Example usage
input_image_path = '1.png'
output_image = convert_image_to_pencil_art(input_image_path)
# cv2.imwrite('path/to/output/pencil_art.jpg', output_image)

cv2.imshow('output_image',output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()