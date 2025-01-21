import cv2
import numpy as np
from PIL import Image

def canny_edge(image, threshold1, threshold2):
    return Image.fromarray(cv2.Canny(np.array(image), threshold1, threshold2))
