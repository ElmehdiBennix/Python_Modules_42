"""Module to test and visualize all image manipulation filters."""

import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red


def main() -> None:
    """Load an image, apply all color filters, and print their docstrings."""
    array = ft_load("../subject/landscape.jpg")
    if array is None:
        return

    # Original Image
    plt.figure("Original")
    plt.imshow(array)
    plt.axis("off")
    plt.show()

    # Inverted Image
    inverted = ft_invert(array)
    plt.figure("Inverted")
    plt.imshow(inverted)
    plt.axis("off")
    plt.show()

    # Red Filter
    red_img = ft_red(array)
    plt.figure("Red Filter")
    plt.imshow(red_img)
    plt.axis("off")
    plt.show()

    # Green Filter
    green_img = ft_green(array)
    plt.figure("Green Filter")
    plt.imshow(green_img)
    plt.axis("off")
    plt.show()

    # Blue Filter
    blue_img = ft_blue(array)
    plt.figure("Blue Filter")
    plt.imshow(blue_img)
    plt.axis("off")
    plt.show()

    # Grey Filter (2D or single channel needs 'gray' cmap)
    grey_img = ft_grey(array)
    plt.figure("Grey Filter")
    plt.imshow(grey_img, cmap="gray")
    plt.axis("off")
    plt.show()

    # Print docstrings
    print("\n--- Function Docstrings ---")
    print(f"ft_invert:\n{ft_invert.__doc__}")
    print(f"ft_red:\n{ft_red.__doc__}")
    print(f"ft_green:\n{ft_green.__doc__}")
    print(f"ft_blue:\n{ft_blue.__doc__}")
    print(f"ft_grey:\n{ft_grey.__doc__}")


if __name__ == "__main__":
    main()
