# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : main.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-09-08 22:15:05
# @Description : Generate random points and plot.
# ----------------------------------------------------------------


from importlib.util import LazyLoader
from tokenize import Double
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import Func

# initial number
x_0 = 1
k = 5

# generate and plot 3D distribution graphics
N3 = 500 # point numbers
X, Y, Z = Func.ThreeD_RandomMakerLC(x_0, N3) # generate
X, Y, Z = np.array(X), np.array(Y), np.array(Z)
Func.Plot3D(X, Y, Z, N3) # Plot


# 3D uniformity test
Func.uniformity_test_3D(k, X, Y, Z, N3)


# generate and plot 2D distribution graphics
N2 = 300 # point numbers
X, Y = Func.TwoD_RandomMakerLC(x_0, N2) # generate
X, Y = np.array(X), np.array(Y)
Func.Plot2D(X, Y, N2) # Plot
