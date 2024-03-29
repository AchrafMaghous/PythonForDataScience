from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load

def zoom(img_arr: np.ndarray, zoom: int | float, starting_xy: tuple = (0, 0)) -> list:
    """
    @param img_arr: numpy.ndarray
    @param zoom: int | float
    @param starting_xy: tuple
    @return: list

    This function takes an image array and zooms in on a specific area of the image. The function takes the image array
    """
    try:
        if img_arr is None:
            raise TypeError
        if not isinstance(img_arr, np.ndarray):
            raise TypeError
        if not isinstance(zoom, (int, float)):
            raise TypeError
        if not isinstance(starting_xy, tuple):
            raise TypeError
        if not all([isinstance(x, int) for x in starting_xy]):
            raise TypeError
        if not all([x >= 0 for x in starting_xy]):
            raise ValueError
        if zoom < 1:
            raise ValueError
        if len(img_arr.shape) != 3:
            raise ValueError
        height, width, _ = img_arr.shape
        new_dimension = min(height, width)
        new_height = int(new_dimension / zoom)
        new_width = int(new_dimension / zoom)
        left, upper = starting_xy
        right = left + new_width
        lower = upper + new_height
        if right > width or lower > height:
            raise AssertionError("Error: zoomed area is out of bounds")
        zoomed_img = img_arr[upper:lower, left:right, 0:1]
        print(f"New shape after slicing: {zoomed_img.shape} or ({zoomed_img.shape[0]}, {zoomed_img.shape[1]})")
        return zoomed_img
    except ValueError:
        print("Error: invalid input value")
        return None
    except TypeError:
        print("Error: invalid input type")
        return None



def main():
    try:
        img_arr = ft_load('animal.jpeg')
        # img_arr is an np.ndarray of the img
        print(img_arr)
        # finding the right zoom and starting pixel value was just a matter of testing a lot of values...
        zoomed = zoom(img_arr, 1.92, (450, 100))
        if zoomed is None:
            return
        print(zoomed)
        plt.imshow(zoomed, cmap='gray')
        plt.show()
    except KeyboardInterrupt:
        plt.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
