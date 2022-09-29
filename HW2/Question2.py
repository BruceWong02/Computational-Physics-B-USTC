# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : Question2.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-09-22 11:50:42
# @Description : This code was desighed for solving the question 2
#   in HW2.
# ----------------------------------------------------------------


from random import uniform
import math, cmath
import PlotAnimationOfHist as PAH


# Breit-Wigner Distribution Case Generator
# f(x) = (Gamma/pi) * 1 / ((x - x_0)^2 + Gamma^2)
# F(x) = 1/2 + (1/pi) * arctan((x-x0)/Gamma)
# F^{-1} (y) = x0 + Gamma * tan(pi*(y-1/2))
def BreitWignerCaseGener(Gamma, x0=0):
    if Gamma <= 0:
        return "Gamma value is illegal !!!"
    return (x0 + Gamma * math.tan(180 * (uniform(0, 1) - 0.5)))


def Sub_question1():
    title = "Breit-Wigner Distribution Case Generator"
    PAH.PlotAnimation(BreitWignerCaseGener, 1, 1, title, yTop=1300, hrange=(-20, 20))
    

def Sub_question2(way):
    I, N = 0., 1000000 # initiation

    # sample and calculate
    if 0 == way:
        # method 1: complex integral
        for i in range(0, N):
            I += math.pi * cmath.sqrt(BreitWignerCaseGener(1))
        I = I / N
        print(f"N = {N}\t\tIntegral = {I}")
    else:
        # method 2: real integral mutiply (1 + i)
        for i in range(0, N):
            I += math.pi * math.sqrt(abs(BreitWignerCaseGener(1)))
        I = I / (2*N)
        print(f"N = {N}\t\tIntegral = {I}*(1+i)")

    
    