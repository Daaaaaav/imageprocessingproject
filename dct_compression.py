import cv2
import numpy as np
from PIL import Image

def dct_compression(image, quality=50):
    np_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    dct = cv2.dct(np.float32(np_img) / 255.0)
    compressed = dct[:quality, :quality]
    return Image.fromarray((compressed * 255).astype('uint8'))
