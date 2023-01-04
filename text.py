# import random
# import matplotlib.pyplot as plt

# N = 2000

# x = [random.uniform(0, 1) for i in range(N)]

# y = [random.uniform(0, 1) for i in range(N)]

# plt.scatter(x, y)
# plt.show()

import matplotlib as mpl
import matplotlib.pyplot as plt

a = [[1.5, 2], [3, 4], [5, 6]]
print(a)
a.reverse()
print(a)

fig, ax = plt.subplots()
plt.imshow(a, cmap='summer')
plt.colorbar()
plt.show()

# from math import fabs


# a = -1.4
# print(abs(a), fabs(a))
