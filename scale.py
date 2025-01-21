from PIL import Image

def scale(image, value): 
    width, height = image.size
    return image.resize((int(width * value / 100), int(height * value / 100)))
