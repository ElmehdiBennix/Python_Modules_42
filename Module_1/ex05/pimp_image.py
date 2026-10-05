from numpy.ma.core import array

from load_image import ft_load
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """dis is invert"""
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    arr_copy = array.copy()
    arr_copy[:,:,1] = 0
    arr_copy[:,:,2] = 0
    # print(f"{arr_copy}")
    return arr_copy

def ft_green(array: np.ndarray) -> np.ndarray:
    arr_copy = array.copy()
    arr_copy[:,:,0] = 0
    arr_copy[:,:,2] = 0
    # print(f"{arr_copy}")
    return arr_copy


def ft_blue(array: np.ndarray) -> np.ndarray:
    arr_copy = array.copy()
    arr_copy[:,:,0] = 0
    arr_copy[:,:,1] = 0
    # print(f"{arr_copy}")
    return arr_copy


def ft_grey(array: np.ndarray) -> np.ndarray:
    arr_copy = array.copy()
    
    arr_copy = (arr_copy[:,:,0] / 3) + (arr_copy[:,:,1] / 3) + (arr_copy[:,:,2] / 3)
    
    return arr_copy

# if __name__ == "__main__":
#     pass