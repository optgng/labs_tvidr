from PIL import Image
from core.rgb_to_ycrcb import calc_rgb_to_ycrcb


def split_to_ycrcb_grey(image: Image) -> (Image, Image, Image):
    width, height = image.size

    y_image = Image.new('L', (width, height))
    cr_image = Image.new('L', (width, height))
    cb_image = Image.new('L', (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            fy, fcr, fcb = calc_rgb_to_ycrcb(r, g, b)
            y_image.putpixel((x, y), int(fy))
            cr_image.putpixel((x, y), int(fcr + 128))
            cb_image.putpixel((x, y), int(fcb + 128))
    return y_image, cr_image, cb_image