from PIL import Image
import os
from utils.logger import get_logger


logger = get_logger(__name__)


def load_image(image_path: str):
    if not os.path.isfile(image_path):
        logger.error(f"File {image_path} not found")
        raise FileNotFoundError

    if not image_path.lower().endswith('.bmp'):
        logger.error(f"File {image_path} is not a BMP image")
        raise ValueError

    try:
        img = Image.open(image_path)
        logger.info(f"Image {image_path} loaded successfully!")
        return img
    except Exception as e:
        logger.error(f"Failed to load image {image_path}: {e}")
        raise RuntimeError

