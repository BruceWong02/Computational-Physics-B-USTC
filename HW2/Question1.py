# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : Problem1.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-09-22 11:50:42
# @Description : This code was desighed for solving the question 1
#   in HW2.
# ----------------------------------------------------------------


from random import uniform
import math
import PlotAnimationOfHist as PAH


# Exponential Decay Distribution Case Generator
# F(x) = 1 - exp(- lamda * x), x belong to [0, + infinite)
# F^{-1} (y) = - ln(1-y) / lamda
def ExpDecayCaseGener(lamda):
    return (- math.log(1 - uniform(0, 1)) / lamda)


def Sub_question1():
    title = "Exponential Decay Distribution Case Generator"
    PAH.PlotAnimation(ExpDecayCaseGener, 1, 1, hTitle=title, yTop=1200)


def Sub_question2():
    I, N = 0., 1000000 # initiation

    # sample and calculate
    for i in range(0, N):
        I += pow(ExpDecayCaseGener(1), 3/2)
    I = I / N

    print(f"N = {N}\t\tIntegral = {I}")

