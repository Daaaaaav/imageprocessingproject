from PIL import Image

def diagonal_flip(image): 
    return image.transpose(Image.TRANSPOSE)
