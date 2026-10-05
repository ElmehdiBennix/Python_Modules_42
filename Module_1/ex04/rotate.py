import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_rotate(img_array: np.ndarray, img_x: tuple, img_y: tuple) -> np.ndarray:

    if not isinstance(img_x, tuple) or not isinstance(img_y, tuple):
        raise TypeError("Error")
    if len(img_x) != 2 or len(img_y) != 2:
        raise TypeError("Error")

    x_start, x_end = img_x
    y_start, y_end = img_y

    if not all(isinstance(v, int) for v in (x_start, x_end, y_start, y_end)):
        raise TypeError("Error")

    h, w = img_array.shape[:2]

    if y_start >= y_end or x_start >= x_end:
        raise ValueError("Error")
    if y_start < 0 or x_start < 0:
        raise IndexError("Error")
    if y_end > h or x_end > w:
        raise IndexError("Error")

    cropped = img_array[y_start:y_end, x_start:x_end, 0:1]

    arr = cropped.squeeze()

    rows, columns = arr.shape

    out = np.empty((columns, rows), dtype=arr.dtype)
    for i in range(rows):
        for j in range(columns):
            out[j, i] = arr[i, j]

    print(f"New shape after Transpose: {out.shape} or {arr.shape}")

    return out


def main() -> None:

    try:
        img_array = ft_load("../subject/animal.jpeg")

        print(img_array)

        cropped = ft_rotate(img_array, img_x=(450, 850), img_y=(100, 500))

        plt.imshow(cropped.squeeze(), cmap="gray")
        plt.show()

    except (TypeError, ValueError, IndexError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
