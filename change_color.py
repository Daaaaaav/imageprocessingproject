import numpy as np
from PIL import Image

def change_color(image, target_color, replacement_color):
    np_img = np.array(image)
    target_color = np.array(target_color, dtype=np.uint8)
    replacement_color = np.array(replacement_color, dtype=np.uint8)
    if np_img.shape[2] == 4:
        target_color = np.append(target_color, 255)
        replacement_color = np.append(replacement_color, 255)
    mask = np.all(np_img[..., :3] == target_color[:3], axis=-1)
    if not np.any(mask):
        return image
    np_img[mask] = replacement_color
    return Image.fromarray(np_img)
