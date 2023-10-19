import cv2
import numpy as np
from scipy.spatial import Delaunay

def convert_to_circle_packing(image_path, circle_radius=5):
    # Load the image
    image = cv2.imread(image_path)

    # Calculate the resized dimensions while preserving the aspect ratio
    height, width = image.shape[:2]
    aspect_ratio = width / height
    target_width = 1000
    target_height = int(target_width / aspect_ratio)

    # Resize the image
    image = cv2.resize(image, (target_width, target_height))

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Generate a grid of points based on the circle radius
    rows, cols = image.shape[:2]
    x = np.arange(0, cols, circle_radius * 2)
    y = np.arange(0, rows, circle_radius * 2)
    grid_x, grid_y = np.meshgrid(x, y)
    points = np.vstack((grid_x.ravel(), grid_y.ravel())).T

    # Perform Delaunay triangulation on the grid points
    triangles = Delaunay(points)

    # Create a blank canvas with the same shape as the image
    canvas = np.zeros_like(image)

    # Iterate over each triangle in the triangulation
    for triangle_indices in triangles.simplices:
        # Get the vertices of the current triangle
        pts = points[triangle_indices]

        # Calculate the mean pixel value of the triangle region
        mean_pixel_value = np.mean(grayscale_image[pts[:, 1], pts[:, 0]])

        # Calculate the centroid of the triangle
        centroid = np.mean(pts, axis=0)

        # Calculate the distance from the centroid to the vertices
        distances = np.linalg.norm(pts - centroid, axis=1)

        # Draw circles with decreasing radii from the centroid to the vertices
        for radius in reversed(distances):
            # Get the color of the corresponding pixel in the original image
            color = image[int(centroid[1]), int(centroid[0])]

            # Draw the circle on the canvas with the original color
            cv2.circle(canvas, tuple(centroid.astype(int)), int(radius), tuple(color.tolist()), -1)

    # Display the original image and the circle packing art
    # cv2.imshow('Original Image', image)
    cv2.imshow('Circle Packing Art', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = '1.png'
circle_radius = 5  # Adjust the circle radius for desired level of detail
convert_to_circle_packing(input_image_path, circle_radius)