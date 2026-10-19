"""Program for image manipulation and transpose/rotate operations."""

import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_rotate(
    img_array: np.ndarray, img_x: tuple, img_y: tuple
) -> np.ndarray:
    """Crop a region of an image and transpose (rotate) its axes.

    Args:
        img_array: The source image as a numpy array.
        img_x: A tuple specifying (x_start, x_end).
        img_y: A tuple specifying (y_start, y_end).

    Returns:
        The transposed/rotated image numpy array, or an empty array on error.
    """
    try:
        if not isinstance(img_array, np.ndarray):
            raise TypeError("img_array must be a numpy ndarray.")
        if not isinstance(img_x, tuple) or not isinstance(img_y, tuple):
            raise TypeError("img_x and img_y must be tuples.")
        if len(img_x) != 2 or len(img_y) != 2:
            raise ValueError("Tuples must contain exactly 2 elements.")

        x_start, x_end = img_x
        y_start, y_end = img_y

        if not all(
            isinstance(v, int) and not isinstance(v, bool)
            for v in (x_start, x_end, y_start, y_end)
        ):
            raise TypeError("Tuple coordinates must be integers.")

        h, w = img_array.shape[:2]

        if y_start < 0 or x_start < 0:
            raise IndexError("Start coordinates cannot be negative.")
        if y_end > h or x_end > w:
            raise IndexError("End coordinates exceed image dimensions.")
        if y_start >= y_end or x_start >= x_end:
            raise ValueError("Start must be strictly less than end.")

        cropped = img_array[y_start:y_end, x_start:x_end, 0:1]
        arr = cropped.squeeze()

        rows, columns = arr.shape
        out = np.empty((columns, rows), dtype=arr.dtype)

        for i in range(rows):
            for j in range(columns):
                out[j, i] = arr[i, j]

        print(f"New shape after Transpose: {out.shape}")
        return out

    except (TypeError, ValueError, IndexError) as error:
        print(f"Error in ft_rotate: {error}")
        return np.array([])


def main() -> None:
    """Load image, rotate a cropped region, and display the result."""
    img_array = ft_load("../subject/animal.jpeg")
    if img_array is None:
        return

    print(img_array)

    cropped = ft_rotate(
        img_array,
        img_x=(450, 850),
        img_y=(100, 500)
    )

    if cropped.size > 0:
        plt.imshow(cropped, cmap="gray")
        plt.show()


if __name__ == "__main__":
    main()
