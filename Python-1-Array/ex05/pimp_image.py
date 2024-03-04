import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    @param array: np.ndarray
    @return: np.ndarray
    
    This function takes an image array and inverts the colors
    """
    inverted_array = 255 - array
    print(inverted_array)
    plt.imshow(inverted_array)
    plt.show()
    return inverted_array

def ft_red(array: np.ndarray) -> np.ndarray:
    """
    @param array: np.ndarray
    @return: np.ndarray
    
    This function takes an image array and removes all colors except red
    """
    red_array = array.copy()
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    print(red_array)
    plt.imshow(red_array)
    plt.show()
    return red_array

def ft_green(array: np.ndarray) -> np.ndarray:
    """
    @param array: np.ndarray
    @return: np.ndarray
    
    This function takes an image array and removes all colors except green
    """
    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    print(green_array)
    plt.imshow(green_array)
    plt.show()
    return green_array

def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    @param array: np.ndarray
    @return: np.ndarray

    This function takes an image array and removes all colors except blue
    """
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    print(blue_array)
    plt.imshow(blue_array)
    plt.show()
    return blue_array

def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    @param array: np.ndarray
    @return: np.ndarray
    
    This function takes an image array and converts it to greyscale
    """
    grey_array = np.mean(array, axis = 2)
    grey_array = np.repeat(grey_array[:,:,np.newaxis], 3, axis=2).astype(np.uint8)
    print(grey_array)
    plt.imshow(grey_array, cmap='gray')
    plt.show()
    return grey_array