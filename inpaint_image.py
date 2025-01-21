import cv2
import numpy as np
from PIL import Image
def inpaint_image(image, mask_path):
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if mask is None:
        raise ValueError("Mask image could not be loaded")
    np_img = np.array(image)
    if np_img.shape[:2] != mask.shape:
        raise ValueError("Mask dimensions do not match image dimensions")
    inpainted = cv2.inpaint(np_img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    return Image.fromarray(inpainted)
