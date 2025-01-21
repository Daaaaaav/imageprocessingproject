def template_matching(image, template_image):
    template = np.array(template_image.convert('L'))
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    if template.shape[0] > gray.shape[0] or template.shape[1] > gray.shape[1]:
        raise ValueError("Template dimensions are larger than image dimensions")
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = template.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(gray, top_left, bottom_right, 255, 2)
    return Image.fromarray(gray)  
