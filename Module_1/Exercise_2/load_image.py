"""Load and inspect JPEG images."""

from pathlib import Path


def ft_load(path: str):
    """Load a JPG or JPEG image, print its shape, and return pixel data."""
    image_path = Path(path)
    if image_path.suffix.lower() not in {".jpg", ".jpeg"}:
        raise ValueError("Unsupported file format. Only .jpg and .jpeg are allowed.")

    try:
        import numpy as np
        from PIL import Image

        with Image.open(image_path) as image:
            rgb_image = image.convert("RGB")
            pixels = np.asarray(rgb_image)
    except ModuleNotFoundError as exc:
        raise ImportError("ft_load requires Pillow and numpy to be installed.") from exc
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {path}") from exc
    except Exception as exc:
        raise ValueError(f"Could not load image '{path}': {exc}") from exc

    print(f"The shape of image is: {pixels.shape}")
    return pixels
