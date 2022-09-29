# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : PlotAnimationOfHist.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-09-20 21:21:31
# @Description : Demonstrate the effect of the case generator by 
#   histogram animation.
# ----------------------------------------------------------------


from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np


def PlotAnimation(generator, out, GenerPar, hTitle=None, yTop=None, hrange=None):

    events = []

    fig1, ax = plt.subplots() # Create figure
    _, _, bar_container = ax.hist(events, 100, range=(-30, 30)) # Create histogram in the figure and get its bar container.

    # initiate data
    def init():
        for rect in bar_container.patches:
            rect.set_height(0)
        return bar_container.patches

    # update function
    def animate(i):
        # generate new data
        for j in range(0, 500):
            events.append(generator(GenerPar))
        # update data
        n, _ = np.histogram(events, 100, range=hrange) # Compute the histogram of the dataset.
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)

        return bar_container.patches
        
    ax.set_title(hTitle) # Set title.
    ax.set_ylim(bottom=0, top=yTop) # set y-axis limit in order to see all figure.
    ani = animation.FuncAnimation(fig1, animate, 20, init_func=init, interval=100, repeat=False, blit=True) # Create animation.

    # Choose a kind of output.
    if 0 == out:
        ani.save(f'figs/test{generator.__name__}.gif', writer='pillow') # save as a gif file.
        print("image saved!")
    else:
        plt.show() # directly show.
