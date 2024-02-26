import numpy as np

def slice_me(family: list, start:int, end: int) -> list:
    #your code here
    fam = np.array(family)
    print('My shape is:', fam.shape)
    res = fam[slice(start, end, 1)]
    print('My new shape is:', res.shape)
    return res.tolist()