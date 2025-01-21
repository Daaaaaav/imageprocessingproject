import numpy as np
import cv2
from PIL import Image


def median_filter(image, ksize):
    if ksize <= 0 or ksize % 2 == 0:
       raise ValueError("Kernel size must be a positive odd number!")
    return Image.fromarray(cv2.medianBlur(np.array(image), ksize))
