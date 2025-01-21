def contrast_stretching(image, lower_percentile=2, upper_percentile=98):
    np_img = np.array(image)
    min_val, max_val = np.percentile(np_img, (lower_percentile, upper_percentile))
    stretched = (np_img - min_val) * (255 / (max_val - min_val))
    stretched = np.clip(stretched, 0, 255)
    return Image.fromarray(stretched.astype('uint8'))