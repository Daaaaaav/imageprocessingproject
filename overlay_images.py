def overlay_images(base_image, overlay_image, position, transparency):
    base_image = base_image.convert("RGBA")
    overlay_image = overlay_image.convert("RGBA")
    overlay_image = overlay_image.resize(base_image.size)
    blended = Image.blend(base_image, overlay_image, transparency)
    return blended
