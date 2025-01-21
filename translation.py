import numpy as np
import cv2
from PIL import Image

def translation(image, tx, ty): 
    np_img = np.array(image)
    height, width = np_img.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_img = cv2.warpAffine(np_img, translation_matrix, (width, height))
    return Image.fromarray(translated_img)
