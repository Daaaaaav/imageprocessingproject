import cv2
import numpy as np
from PIL import Image

def pixel_division(image1, image2):
    np_img1 = np.array(image1)
    np_img2 = np.array(image2)
    result = cv2.divide(np_img1, np_img2)
    return Image.fromarray(result)
