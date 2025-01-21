import cv2
import numpy as np
from PIL import Image
def feature_detection(image, method='sift'):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)  
    if method == 'sift':
        sift = cv2.SIFT_create()
        keypoints, descriptors = sift.detectAndCompute(gray, None)
    elif method == 'orb':
        orb = cv2.ORB_create()
        keypoints, descriptors = orb.detectAndCompute(gray, None)
    result = cv2.drawKeypoints(gray, keypoints, None)
    return Image.fromarray(result)
