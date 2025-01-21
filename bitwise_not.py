import numpy as np
import cv2
from PIL import Image

def bitwise_not(image):
    np_img = np.array(image)
    result = cv2.bitwise_not(np_img)
    return Image.fromarray(result)