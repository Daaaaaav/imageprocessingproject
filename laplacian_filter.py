def laplacian_filter(image):
    laplacian = cv2.Laplacian(np.array(image), cv2.CV_64F)
    abs_laplacian = np.absolute(laplacian)
    laplacian_8u = np.uint8(abs_laplacian)
    return Image.fromarray(laplacian_8u)
