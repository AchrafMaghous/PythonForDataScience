import numpy as np

def slice_me(family: list, start:int, end: int) -> list:
    #your code here
    try:
        if not isinstance(family, list):
            raise TypeError
        if not isinstance(start, int):
            raise TypeError
        if not isinstance(end, int):
            raise TypeError
        fam = np.array(family)
        if fam.ndim != 2:
            raise AssertionError("Error: family must be a 2D list")
        print('My shape is:', fam.shape)
        res = fam[slice(start, end, 1)]
        print('My new shape is:', res.shape)
        return res.tolist()
    except TypeError:
        print('Error: family must be a list and start and end must be integers')