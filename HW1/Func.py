# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : Func.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-09-09 14:17:28
# @Description : Define functions including Plot, RPG(Random Point 
#                Generator) and uniformity_test_3D.
#                
#                Plot is used to plot the 3D or 2D figures.
#
#                The RPG here, with Linear Congruence method, can 
#                generate 3D or 2D random points.
# 
#                Uniformity_test_3D can calculate chi-square for 
#                datas in 3D.
# ----------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt 


# 3D point generator
# N is the number of point
def ThreeD_RandomMakerLC(x, N):
    a, c, m, i = 137, 187, 256, 0
    X, Y, Z = [], [], []

    # Create num
    while i < N:
        X.append(x/m)
        y = (a * x + c) % m
        Y.append(y/m)
        z = (a * y + c) % m
        Z.append(z/m)        
        x = (a * z + c) % m

        i += 1

    return X, Y, Z

# 2D points generate
def TwoD_RandomMakerLC(x, N):
    a, c, m, i = 137, 187, 256, 0
    X, Y = [], []

    # Create num
    while i < N:
        X.append(x/m)
        y = (a * x + c) % m
        Y.append(y/m)      
        x = (a * y + c) % m

        i += 1

    return X, Y

def Plot3D(X, Y, Z, N3):
    fig3 = plt.figure()
    ax3 = plt.axes(projection='3d')
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    ax3.set_zlabel("Z")

    LinNum3 = np.linspace(1, N3+1, N3)
    ax3.scatter3D(X, Y, Z, s=LinNum3, alpha=0.5, c=LinNum3)
    ax3.set_title('3D Scatter Plot')
    plt.show()

def Plot2D(X, Y, N2):
    LinNum2 = np.linspace(1, N2+1, N2)

    plt.scatter(X, Y, s=LinNum2, alpha=0.5, c=LinNum2)
    plt.show()


def uniformity_test_3D(k, X, Y, Z, N3):
    l = 1/k

    # divide 3D space to kxkxk
    xyz = [[[0 for iz in range(k)] for iy in range(k)] for ix in range(k)]

    # count
    for i in range(N3):
        xyz[int(X[i]//l)][int(Y[i]//l)][int(Z[i]//l)] += 1

    # calculate chi-square
    chi_square_3D = 0.
    for ix in range(k):
        for iy in range(k):
            for iz in range(k):
                chi_square_3D += (k*k*k / N3) * (xyz[ix][iy][iz] - N3 / (k*k*k)) * (xyz[ix][iy][iz] - N3 / (k*k*k))

    print(f"for 3D\nN = {N3} \t k = {k} \t chi-square = {chi_square_3D}\nObey the distribution of chi-square({(k-1)*(k-1)*(k-1)})")