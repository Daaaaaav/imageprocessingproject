import cv2
import numpy as np
from PIL import Image

def boundary_extraction(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    eroded = cv2.erode(gray, np.ones((3, 3), np.uint8))
    boundary = gray - eroded
    return Image.fromarray(boundary)
