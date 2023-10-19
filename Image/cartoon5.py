import cv2
import numpy as np

def convert_image_to_pixel_art(image_path, pixel_size):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))
    # Resize the image to the desired pixel size
    image_resized = cv2.resize(image, (pixel_size, pixel_size))

    # Apply color quantization
    pixel_art = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
    pixel_art = pixel_art.reshape(-1, 3)
    pixel_art = np.float32(pixel_art)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)
    _, labels, palette = cv2.kmeans(pixel_art, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    palette = np.uint8(palette)
    quantized_image = palette[labels.flatten()]
    quantized_image = quantized_image.reshape(image_resized.shape)
    quantized_image = cv2.cvtColor(quantized_image, cv2.COLOR_RGB2BGR)

    return quantized_image

# Example usage
input_image_path = '1.png'
pixel_size = 600  # Specify the desired pixel size
output_image = convert_image_to_pixel_art(input_image_path, pixel_size)
# cv2.imwrite('path/to/output/pixel_art.jpg', output_image)

cv2.imshow('output_image',output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()