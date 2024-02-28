from PIL import Image
import numpy as np

def ft_load(path : str) -> np.ndarray:
    """
    @param path: str
    @return: np.ndarray

    This function takes a path to an image and returns the image as a numpy array
    """
    try:
        if not isinstance(path, str):
            raise TypeError
        if path == '':
            raise ValueError
        img = Image.open(path)
        imgArray = np.array(img)
        return imgArray
    except PermissionError:
        print('Error: permission denied')
    except TypeError:
        print('Error: path must be a string')
    except ValueError:
        print('Error: path must not be empty')
    