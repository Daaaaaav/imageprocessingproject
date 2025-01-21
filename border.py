from PIL import Image, ImageOps

def add_border(image, border_size, border_color):
    border_color = tuple(int(border_color[i:i+2], 16) for i in (0, 2, 4))
    return ImageOps.expand(image, border=border_size, fill=border_color)
