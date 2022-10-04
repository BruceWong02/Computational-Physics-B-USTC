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


def GaussFunc(x, mu, sigma):
    """
    Calculate gauss distribution density function value
    """
    return pow(math.e, -(x-mu)*(x-mu)/(2*sigma*sigma)) / (math.sqrt(2*math.pi) * sigma) 


def Gauss_Metro(nSample, mu=0, sigma=1, delta=1, SelfAdopt=0):
    """
    Metropolis method for Gauss distribution sampling
    args:
        nSample: number of Samples
        delta: step length
        SelfAdopt: 0 for stopping iteration by number of samples;
                else for stopping iteration by the condition
                of equilibrium: <(x-mu)^2> approx to sigma^2 
                        while it's value is used as the error
    """
    NSample = 0 # real number of samples
    flag = 0

    x = mu
    xList = [x]
    Acceptance = 0
    VarX = 0 # <(x-mu)^2>

    seed(time())
    while True:
        NSample += 1

        eta = uniform(-delta, delta)
        r = GaussFunc(x+eta, mu, sigma) / GaussFunc(x, mu, sigma)
        if (r >= 1) or (uniform(0, 1) <= r):
            x = x + eta
            xList.append(x)

            Acceptance += 1
            VarX += (x - mu)*(x - mu)

        # acceptance can be used as the number of generated number
        if (NSample > 10000) and SelfAdopt and (abs(VarX/Acceptance - sigma*sigma) <= SelfAdopt):
            flag += 1
        else:
            flag = 0
        if NSample >= nSample or flag >= 5: # nSample here is used as the uplimit
            break

    VarX /= Acceptance
    
    # Acceptance here is number of walk, Acceptance/NSample is acceptance.
    return xList, Acceptance/NSample, VarX, Acceptance, NSample
    
