import numpy as np
from PIL import Image
def crop_image(image, x, y, width, height):
    np_img = np.array(image)
    img_height, img_width = np_img.shape[:2]
    x = max(0, min(int(x), img_width))
    y = max(0, min(int(y), img_height))
    width = max(1, min(int(width), img_width - x))
    height = max(1, min(int(height), img_height - y))
    cropped_img = np_img[y:y+height, x:x+width]
    return Image.fromarray(cropped_img)
