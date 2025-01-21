from PIL import ImageEnhance
def brightness(image, value):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(value / 50)
