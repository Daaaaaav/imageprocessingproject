from PIL import Image, ImageOps

def negative(image): 
    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        rgb_image = Image.merge('RGB', (r, g, b))
        inverted_image = ImageOps.invert(rgb_image)
        r, g, b = inverted_image.split()
        return Image.merge('RGBA', (r, g, b, a))
    else:
        return ImageOps.invert(image)
