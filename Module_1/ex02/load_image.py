"""Module to load and display RGB image dimensions."""

from pathlib import Path

import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray | None:
    """Load an image file, print its shape, and return its pixel array.

    Args:
        path: File path string pointing to a .jpg or .jpeg image.

    Returns:
        A NumPy array of the image pixels, or None on error.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")

        image_path = Path(path)

        if not image_path.is_file():
            raise FileNotFoundError(f"File not found: {path}")

        if image_path.suffix.lower() not in [".jpg", ".jpeg"]:
            raise ValueError(
                "Unsupported format. Only (.jpg, .jpeg) are supported."
            )

        with Image.open(image_path) as img:
            img_rgb = img.convert("RGB")
            img_array = np.array(img_rgb)

            print(f"The shape of image is: {img_array.shape}")
            return img_array

    except (
        FileNotFoundError,
        ValueError,
        TypeError,
        UnidentifiedImageError,
    ) as error:
        print(f"Error in ft_load: {error}")
        return None
