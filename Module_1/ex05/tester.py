import matplotlib.pyplot as plt
from load_image import ft_load
from numpy import array
from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red

array = ft_load("../subject/landscape.jpg")

plt.imshow(array.squeeze(), cmap="gray")
plt.show()

test = ft_invert(array)

plt.imshow(test.squeeze(), cmap="gray")
plt.show()

test = ft_red(array)

plt.imshow(test.squeeze(), cmap="gray")
plt.show()

test = ft_green(array)

plt.imshow(test.squeeze(), cmap="gray")
plt.show()

test = ft_blue(array)

plt.imshow(test.squeeze(), cmap="gray")
plt.show()

test = ft_grey(array)

plt.imshow(test.squeeze(), cmap="gray")
plt.show()


print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_red.__doc__)
print(ft_grey.__doc__)