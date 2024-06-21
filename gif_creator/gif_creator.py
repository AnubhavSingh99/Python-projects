import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = [r"Python projects\gif_creator\img1.jpg",
             r"Python projects\gif_creator\img2.jpg"]
images = []
common_size = (500, 500)  # Set this to your desired common size

try:
    for filename in filenames:
        img = Image.open(filename)
        if img.size != common_size:
            img = img.resize(common_size)  # Resize the image
        images.append(np.array(img))  # Convert the PIL image to a NumPy array

    iio.imwrite('anubhav.gif', images, duration=500, loop=0)
    print("GIF created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")