import cv2
import numpy as np
from PIL import Image

def morphological_operations(image, operation='dilation', kernel_size=5):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if operation == 'dilation':
        result = cv2.dilate(gray, kernel)
    elif operation == 'erosion':
        result = cv2.erode(gray, kernel)
    elif operation == 'opening':
        result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    elif operation == 'closing':
        result = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    return Image.fromarray(result)
