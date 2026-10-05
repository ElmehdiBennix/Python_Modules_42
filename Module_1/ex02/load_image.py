from pathlib import Path

import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:

    image_path = Path(path)

    if image_path.suffix.lower() not in [".jpg", ".jpeg"]:
        raise ValueError("Error: image format must be supported (.jpg, .jpeg)")

    if not image_path.is_file():
        raise ValueError("Error: image dosnt exist")

    with Image.open(image_path) as img:
        img_rgb = img.convert("RGB")
        img_array = np.array(img_rgb)

        print(f"The shape of image is: {img_array.shape}")

        return img_array


print(
    ft_load(
        "/home/rambeau/Projects/Python_Modules_42/Module_1/subject/animal.jpeg"
    )
)