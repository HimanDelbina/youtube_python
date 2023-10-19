import cv2
import numpy as np
from scipy.spatial import Delaunay

def convert_to_triangle_art(image_path, num_triangles=5000):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1000, 1000))
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Generate random points for triangulation within the image bounds
    height, width = grayscale_image.shape[:2]
    points = np.random.randint(0, max(width, height), size=(num_triangles * 3, 2))
    # points = np.random.randint(0, min(width, height), size=(num_triangles * 3, 2))

    # Perform Delaunay triangulation on the random points
    triangles = Delaunay(points)

    # Create a blank canvas with black background
    canvas = np.zeros_like(image)

    # Iterate over each triangle in the triangulation
    for triangle_indices in triangles.simplices:
        # Get the vertices of the current triangle
        pts = points[triangle_indices]

        # Calculate the mean color of the triangle region
        valid_pts = pts[pts[:, 0] < width]
        valid_pts = valid_pts[valid_pts[:, 1] < height]
        mean_color = np.mean(image[valid_pts[:, 1], valid_pts[:, 0]], axis=0)

        # Draw the triangle on the canvas with the mean color as the fill color
        cv2.fillPoly(canvas, [pts.reshape((-1, 1, 2))], tuple(mean_color.astype(int).tolist()))

    # Display the original image and the triangle art
    cv2.imshow('Original Image', image)
    cv2.imshow('Triangle Art', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
num_triangles = 20000  # Adjust the number of triangles for desired level of detail
convert_to_triangle_art(input_image_path, num_triangles)