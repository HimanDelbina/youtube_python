import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# Load the pre-trained sketch generation model
model_path = "models/colorization_model.py"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load(model_path, map_location=device)["model"].to(device)
model.eval()


def convert_to_sketch(image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    image_tensor = transform(image).unsqueeze(0).to(device)

    # Generate the sketch using the pre-trained model
    with torch.no_grad():
        sketch_tensor = model(image_tensor)

    # Convert the sketch tensor to an image
    sketch = sketch_tensor.squeeze().cpu().numpy().transpose(1, 2, 0)
    sketch = (sketch + 1) / 2.0  # Rescale values from [-1, 1] to [0, 1]
    sketch = np.clip(sketch, 0, 1)  # Clip values to [0, 1]
    # Convert to 8-bit unsigned integer
    sketch = (sketch * 255).astype(np.uint8)

    # Display the sketch
    cv2.imshow("Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Path to the image you want to convert to a sketch
image_path = "1.png"

# Convert the image to a sketch
convert_to_sketch(image_path)