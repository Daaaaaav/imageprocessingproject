from PIL import ImageEnhance

def contrast(image, value):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(value / 50)
