from PIL import Image
import cv2
import numpy as np

def mean_filter(image, ksize):
    return Image.fromarray(cv2.blur(np.array(image), (ksize, ksize)))
