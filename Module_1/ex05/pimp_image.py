"""Module for image color manipulations"""

import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert the colors of an image array by subtracting each pixel from 255.

    Args:
        array: A 3D numpy array representing the image pixels.

    Returns:
        The color-inverted numpy array, with the same shape as the input.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy ndarray.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError(
                "Input must be a 3D array with 3 colour channels.")
        return 255 - array
    except (TypeError, ValueError, IndexError) as error:
        print(f"Error in ft_invert: {error}")
        return np.array([])


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of an image, zeroing out green and blue.

    Args:
        array: A 3D numpy array representing the image pixels.

    Returns:
        A numpy array with only the red channel active.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy ndarray.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError(
                "Input must be a 3D array with 3 colour channels.")
        arr_copy = array.copy()
        arr_copy[:, :, 1] = 0
        arr_copy[:, :, 2] = 0
        return arr_copy
    except (TypeError, ValueError, IndexError) as error:
        print(f"Error in ft_red: {error}")
        return np.array([])


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel of an image, zeroing out red and blue.

    Args:
        array: A 3D numpy array representing the image pixels.

    Returns:
        A numpy array with only the green channel active.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy ndarray.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError(
                "Input must be a 3D array with 3 colour channels.")
        arr_copy = array.copy()
        arr_copy[:, :, 0] = 0
        arr_copy[:, :, 2] = 0
        return arr_copy
    except (TypeError, ValueError, IndexError) as error:
        print(f"Error in ft_green: {error}")
        return np.array([])


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of an image, zeroing out red and green.

    Args:
        array: A 3D numpy array representing the image pixels.

    Returns:
        A numpy array with only the blue channel active.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy ndarray.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError(
                "Input must be a 3D array with 3 colour channels.")
        arr_copy = array.copy()
        arr_copy[:, :, 0] = 0
        arr_copy[:, :, 1] = 0
        return arr_copy
    except (TypeError, ValueError, IndexError) as error:
        print(f"Error in ft_blue: {error}")
        return np.array([])


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to greyscale by averaging its three channels.

    The subject only allows the '=' and '/' operators for this function, so the
    average is computed with numpy's mean() and written back into the three
    channels of a copy of the input. The shape of the image is preserved.

    Args:
        array: A 3D numpy array representing the image pixels.

    Returns:
        A numpy array with the same shape as the input, in greyscale.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy ndarray.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError(
                "Input must be a 3D array with 3 colour channels.")
        grey = array.copy()
        value = np.mean(array, axis=2)
        grey[:, :, 0] = value
        grey[:, :, 1] = value
        grey[:, :, 2] = value
        return grey
    except (TypeError, ValueError, IndexError) as error:
        print(f"Error in ft_grey: {error}")
        return np.array([])
