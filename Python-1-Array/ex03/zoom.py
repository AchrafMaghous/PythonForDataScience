from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def zoom_on_img(path: str) -> list:
    """
    @param path: path to the image
    @return zoomed_img as a list

    This function takes an image and returns a zoomed version in grayscale of it to a shape of (400, 400, 1) or (400, 400)
    """
    img_as_list = ft_load(path)
    img = np.array(img_as_list)
    img = img[:, :, 0]
    img = img[::2, ::2]
    return img.tolist()

def main():
    zoom_on_img('animal.jpeg')

if __name__ == "__main__":
    main()