import cv2
import numpy as np
from PIL import Image

def sobel_filter(image, dx, dy, ksize):
    sobel = cv2.Sobel(np.array(image), cv2.CV_64F, dx, dy, ksize)
    abs_sobel = np.absolute(sobel)
    sobel_8u = np.uint8(abs_sobel)
    return Image.fromarray(sobel_8u)
