# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------
# @copyright (C), 2022, Bruce Wong, All rights reserved.
# @File Name   : main.py
# @Author      : Bruce Wong
# @Version     : 
# @Date        : 2022-09-22 11:50:42
# @Description : The main file of this computational physics 
#   homework. You can choose functions to solve each problem. 
#   For details about functions, please check it out in the 
#   relavent files.
# ----------------------------------------------------------------


import Question1 as Q1
import Question2 as Q2


while True:
    print("**********************************************")
    flag = input(f"1-Q1\t2-Q2\t(else)-quit\nPlease input the problem you wanna solve:")

    if "1" == flag:
        Q1.Sub_question1()
        Q1.Sub_question2()
    elif "2" == flag:
        Q2.Sub_question1()
        Q2.Sub_question2(1)
    else:
        print("Thanks for Using!")
        break

