def cyano_filter(image, filter_type):
    cyanotype_filter = np.array([[0.272, 0.534, 0.131],
                                     [0.349, 0.686, 0.168],
                                     [0.393, 0.769, 0.189]])
    np_img = np.array(image)
    filtered_img = np.dot(np_img[..., :3], cyanotype_filter.T)
    filtered_img = np.clip(filtered_img, 0, 255)
    return Image.fromarray(filtered_img.astype('uint8')) 
