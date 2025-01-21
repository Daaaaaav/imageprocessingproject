def skeletonization(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    skeleton = np.zeros_like(binary)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    while True:
        open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, element)
        temp = cv2.subtract(binary, open)
        eroded = cv2.erode(binary, element)
        skeleton = cv2.bitwise_or(skeleton, temp)
        binary = eroded.copy()
        if cv2.countNonZero(binary) == 0:
            break
    return Image.fromarray(skeleton)
 
