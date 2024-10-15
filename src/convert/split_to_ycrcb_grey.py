from PIL import Image
from core.rgb_to_ycrcb import calc_rgb_to_ycrcb
from utils.logger import get_logger


logger = get_logger(__name__)


def split_to_ycrcb_grey(image: Image) -> (Image, Image, Image):
    width, height = image.size

    logger.debug(f"Image size: {width}x{height}")
    logger.info("Creating YCrCb images...")

    y_image = Image.new('L', (width, height))
    cr_image = Image.new('L', (width, height))
    cb_image = Image.new('L', (width, height))

    logger.info("Converting pixels...")
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            fy, fcr, fcb = calc_rgb_to_ycrcb(r, g, b)
            y_image.putpixel((x, y), int(fy))
            cr_image.putpixel((x, y), int(fcr + 128))
            cb_image.putpixel((x, y), int(fcb + 128))
    return y_image, cr_image, cb_image