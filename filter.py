import numpy as np
from PIL import Image

def apply_filter(image, filter_type):
    if filter_type == 'sepia':
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                 [0.349, 0.686, 0.168],
                                 [0.272, 0.534, 0.131]])
        np_img = np.array(image)
        filtered_img = np.dot(np_img[..., :3], sepia_filter.T)
        filtered_img = np.clip(filtered_img, 0, 255)
        return Image.fromarray(filtered_img.astype('uint8'))
