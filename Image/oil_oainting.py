import cv2

def convert_to_oil_painting(image_path, size=7, range=0.5):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the stylization filter
    stylized_image = cv2.stylization(image, sigma_s=size, sigma_r=range)

    # Display the original image and the oil painting effect
    cv2.imshow('Original Image', image)
    cv2.imshow('Oil Painting Effect', stylized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
size = 7  # Adjust the size for desired level of detail
range = 0.5  # Adjust the range for desired effect strength
convert_to_oil_painting(input_image_path, size, range)