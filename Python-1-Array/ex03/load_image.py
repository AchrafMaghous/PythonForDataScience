from PIL import Image
import numpy as np

def ft_load(path : str) -> np.ndarray:
    try:
        if not isinstance(path, str):
            raise TypeError
        if path == '':
            raise ValueError
        img = Image.open(path)
        imgArray = np.array(img)
        print(f"The shape of image is: {imgArray.shape}")
        return imgArray
    except PermissionError:
        print('Error: permission denied')
    except TypeError:
        print('Error: path must be a string')
    except ValueError:
        print('Error: path must not be empty')
