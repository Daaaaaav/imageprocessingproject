from PIL import Image

def flip(image, direction): 
    if direction == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == 'vertical':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        return image.transpose(Image.ROTATE_180)


