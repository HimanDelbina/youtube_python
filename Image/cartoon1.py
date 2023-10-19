import cv2
# from Cartoonizer import Cartoonizer

def convert_to_cartoon(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a bilateral filter to reduce noise while preserving edges
    filtered = cv2.bilateralFilter(gray, 9, 75, 75)

    # Perform adaptive thresholding to create a binary image
    _, thresholded = cv2.threshold(filtered, 150, 255, cv2.THRESH_BINARY)

    # Create a color version of the thresholded image
    color = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)

    # Apply a bitwise and operation to retain color information from the original image
    cartoonized = cv2.bitwise_and(image, color)

    cv2.imshow('Cartoon Effect', cartoonized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
convert_to_cartoon(input_image_path)