import cv2
import numpy as np
from PIL import Image

def global_thresholding(image, threshold):
    _, thresh_img = cv2.threshold(np.array(image), threshold, 255, cv2.THRESH_BINARY)
    return Image.fromarray(thresh_img)
