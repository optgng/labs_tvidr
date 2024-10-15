from PIL import Image
from utils.logger import get_logger

logger = get_logger(__name__)


def save_image(image: Image, image_path: str):
    if not isinstance(image, Image.Image):
        logger.error(f"Invalid image type: {type(image)}")
        raise TypeError

    if not image_path.lower().endswith('.bmp'):
        logger.error(f"File {image_path} is not a BMP image")
        raise ValueError

    try:
        image.save(image_path, format='BMP')
        logger.info(f"Image {image_path} saved successfully!")
    except Exception as e:
        logger.error(f"Failed to save image {image_path}: {e}")
        raise RuntimeError