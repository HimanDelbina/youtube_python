import cv2
import numpy as np

def convert_image_to_brush_art(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a median blur to reduce noise and create brush strokes
    blurred_image = cv2.medianBlur(gray_image, 25)
    
    # Invert the blurred image
    inverted_image = 255 - blurred_image
    
    # Convert the inverted image back to BGR color space
    inverted_image_bgr = cv2.cvtColor(inverted_image, cv2.COLOR_GRAY2BGR)
    
    # Blend the inverted image with the original image using the "multiply" blending mode
    brush_art = cv2.multiply(image, inverted_image_bgr, scale=1/255)
    
    return brush_art

# Example usage
input_image_path = '1.png'
output_image = convert_image_to_brush_art(input_image_path)
# cv2.imwrite('path/to/output/brush_art.jpg', output_image)

cv2.imshow('output_image',output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()