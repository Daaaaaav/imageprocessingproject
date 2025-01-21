import numpy as np
import cv2
from PIL import Image
from scipy.signal import wiener

def noise_reduction(image, method='gaussian'):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    
    if method == 'gaussian':
        result = cv2.GaussianBlur(gray, (5, 5), 0)
    elif method == 'wiener':
        result = wiener(gray)
    else:
        raise ValueError("Unknown method: Choose 'gaussian' or 'wiener'")
    
    return Image.fromarray(result)
