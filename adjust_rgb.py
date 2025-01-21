import numpy as np
from PIL import Image

def adjust_rgb(image, red_factor=1.0, green_factor=1.0, blue_factor=1.0):
    np_img = np.array(image)
    r, g, b = np_img[..., 0], np_img[..., 1], np_img[..., 2]
    r = np.clip(r * red_factor, 0, 255)
    g = np.clip(g * green_factor, 0, 255)
    b = np.clip(b * blue_factor, 0, 255)
    adjusted_img = np.stack([r, g, b], axis=-1)
    return Image.fromarray(adjusted_img.astype('uint8'))

