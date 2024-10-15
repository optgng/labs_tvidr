from utils.logger import get_logger
from services.load_image import load_image
from services.save_image import save_image
from convert.split_to_ycrcb_grey import split_to_ycrcb_grey

logger = get_logger(__name__)


def main():
    image_path = input("Enter image path: ")
    logger.debug(f"Image path: {image_path}")
    bmp_image = load_image(image_path)

    y_image, cr_image, cb_image = split_to_ycrcb_grey(bmp_image)

    save_image(y_image, 'data/y.bmp')
    save_image(cr_image, 'data/cr.bmp')
    save_image(cb_image, 'data/cb.bmp')


if __name__ == '__main__':
    main()
