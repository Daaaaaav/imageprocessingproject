def custom_filter(image, kernel):
    np_img = np.array(image)
    kernel = np.array(kernel, dtype=np.float32)
    filtered_img = cv2.filter2D(np_img, -1, kernel)
    return Image.fromarray(filtered_img)
