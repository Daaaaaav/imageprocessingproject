from PIL import Image
def blend_images(image1, image2, alpha):
    return Image.blend(image1, image2, alpha)
