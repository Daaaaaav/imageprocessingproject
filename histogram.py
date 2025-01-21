import cv2
import numpy as np
from PIL import Image

def histogram_equalization(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    equalized = cv2.equalizeHist(gray)
    return Image.fromarray(equalized)
