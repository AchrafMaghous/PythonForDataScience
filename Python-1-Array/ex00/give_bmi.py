import sys
import numpy as np


def check_is_int_or_float(arr: list[int | float]) -> bool:
    """
    @param arr: list[int | float]
    @return: bool
    @description: Check if the elements of the list are either int or float.
    """
    for i in arr:
        if not isinstance(i, (int, float)):
            return False
    return True


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    @param height: list[int | float]
    @param weight: list[int | float]
    @return: list[int | float]
    @description: Calculate BMI from the given height and weight.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError
        if not height or not weight:
            print("Error: The lists should not be empty.")
            sys.exit(1)
        if len(height) != len(weight):
            print("Error: The length of the two lists should be the same.")
            sys.exit(1)
        if not check_is_int_or_float(height) or not check_is_int_or_float(weight):
            print("Error: The elements of the lists should be either int or float.")
            sys.exit(1)
        height_arr = np.array(height)
        weight_arr = np.array(weight)
        bmi = weight_arr / (height_arr ** 2)
        return bmi.tolist()
    except TypeError:
        print('Error: height and weight must be lists')

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_arr = np.array(bmi)
    return (bmi_arr > limit).tolist()

