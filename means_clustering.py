import numpy as np
import cv2
from PIL import Image

def k_means_clustering(image, K):
    Z = np.array(image).reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    return Image.fromarray(res.reshape((image.size[1], image.size[0], 3)))
