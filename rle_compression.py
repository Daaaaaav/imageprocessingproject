import numpy as np

def rle_compression(image):
    np_img = np.array(image).flatten()
    compressed = []
    count = 1
    for i in range(1, len(np_img)):
        if np_img[i] == np_img[i-1]:
            count += 1
        else:
            compressed.append((np_img[i-1], count))
            count = 1
    compressed.append((np_img[-1], count))
    return compressed
