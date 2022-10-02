# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : RandomWalk.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-10-02 16:00:20
# @Description : Some application of random walk.
# ----------------------------------------------------------------


import math
from random import seed, uniform
from time import time


# Calculate gauss distribution density function value
def GaussFunc(x, mu, sigma):
    return pow(math.e, -(x-mu)*(x-mu)/(2*sigma*sigma)) / (math.sqrt(2*math.pi) * sigma) 


# Metropolis method for Gauss distribution sampling
def Gauss_Metro(nWalk, mu=0, sigma=1, delta=1, SelfAdopt=0):
    """
    nWalk: number of random walk
    delta: step length
    SelfAdopt: 0 for stopping iteration by number of walk;
               else for stopping iteration by the condition
               of equilibrium: <(x-mu)^2> approx to sigma^2 
                    while it's value is used as the error
    """
    NWalk = 0 # real number of walk

    x = mu
    xList = [x]
    Acceptance = 0
    VarX = 0 # <(x-mu)^2>

    seed(time())
    while True:
        NWalk += 1

        eta = uniform(-delta, delta)
        r = GaussFunc(x+eta, mu, sigma) / GaussFunc(x, mu, sigma)
        if (r >= 1) or (uniform(0, 1) <= r):
            x = x + eta
            xList.append(x)

            Acceptance += 1
            VarX += (x - mu)*(x - mu)

        # acceptance can be used as the number of generated number
        if (NWalk > 100) and SelfAdopt and (abs(VarX/Acceptance - sigma*sigma) <= SelfAdopt):
            break
        if NWalk >= nWalk: # nWalk here is used as the uplimit
            break

    VarX /= Acceptance
    Acceptance /= NWalk

    return xList, Acceptance, VarX, NWalk

