# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : main.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-10-02 15:38:21
# @Description : Using Metropolis random walk generate random 
#   numbers obeying Gauss distribution.
# ----------------------------------------------------------------


import RandomWalk
import matplotlib.pyplot as plt


mu = 0
sigma = 1
delta = 1

# # an example
# RandNums, Accept, VarX, RealWalk = RandomWalk.Gauss_Metro(
#     1000000, mu, sigma, delta, SelfAdopt=0.3)

# # Plot
# plt.hist(RandNums, bins=100, range=[-15, 15], density=True, label="Generated Distribution")
# Y = [RandomWalk.GaussFunc(-15+0.1*x, mu, sigma) for x in range(300)]
# plt.plot([-15+0.1*x for x in range(300)], Y, label="Theoratical Distribution")

# plt.legend()
# plt.text(-14, 0.12, f"Acceptance: {Accept}") # text use the same coordinate as the plot
# plt.text(-14, 0.10, f"$\langle (x-\mu)^2 \rangle $: {VarX}")
# plt.text(-14, 0.08, f"Real number of walk: {RealWalk}")
# plt.show()

# ----------------------------------------------------

# check relationship of delta and number of walk when 
# arrive the condition of equilibrium
RealWalks = []
deltaMid, deltaNum, deltaStep = 4, 200, 0.01

for delta in range(1, deltaNum):
    delta = deltaStep*delta + deltaMid - deltaStep*deltaNum / 2
    RandNums, Accept, VarX, RealWalk = RandomWalk.Gauss_Metro(
        500000, mu, sigma, delta, SelfAdopt=0.1)
    RealWalks.append(RealWalk)

# Plot
plt.clf()
plt.plot([deltaMid-deltaStep*deltaNum/2+i*deltaStep for i in range(1, deltaNum)], RealWalks)
plt.xlabel("$\delta$")
plt.ylabel("number of walk")
plt.show()

