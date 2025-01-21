def pixel_addition(image1, image2):
    np_img1 = np.array(image1)
    np_img2 = np.array(image2)
    result = cv2.add(np_img1, np_img2)
    return Image.fromarray(result)
 
 
