import numpy as np
import cv2
from PIL import Image

def bitwise_xor(image1, image2):
    np_img1 = np.array(image1)
    np_img2 = np.array(image2)
    result = cv2.bitwise_xor(np_img1, np_img2)
    return Image.fromarray(result)
