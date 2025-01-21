import cv2
import numpy as np
from PIL import Image
def bitwise_and(image1, image2):
    np_img1 = np.array(image1)
    np_img2 = np.array(image2)
    result = cv2.bitwise_and(np_img1, np_img2)
    return Image.fromarray(result)
