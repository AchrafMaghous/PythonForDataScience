from load_image import ft_load
import matplotlib.pyplot as plt
from pimp_image import *

array = ft_load("landscape.jpeg")

# showing the original array
# plt.imshow(array)
# plt.show()

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

# printing docs

print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
