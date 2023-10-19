from PIL import Image
import cv2

def convert_image_to_art(image_path):
    # Open the image file
    image = Image.open(image_path)
    image = cv2.resize(image, (1500, 1000))
    
    # Convert the image to RGB mode (if it's not already)
    image = image.convert('RGB')
    
    # Get the width and height of the image
    width, height = image.size
    
    # Create a new blank image with the same dimensions
    art_image = Image.new('RGB', (width, height))
    
    # Iterate over each pixel in the original image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = image.getpixel((x, y))
            
            # Manipulate the color values to create an artistic effect
            # Here, we're simply swapping the red and blue color channels
            new_r = b
            new_g = g
            new_b = r
            
            # Set the color of the corresponding pixel in the art image
            art_image.putpixel((x, y), (new_r, new_g, new_b))
    
    return art_image

# Example usage
input_image_path = '1.png'
output_image = convert_image_to_art(input_image_path)
# output_image.save('F:\Python\image_test_save/image.png')

# cv2.imshow('output_image',output_image)
# cv2.imwrite("D:\Python36\siva_written.jpg",pencil_jc)
# cv2.waitKey(0)
# cv2.destroyAllWindows()