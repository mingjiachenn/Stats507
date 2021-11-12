# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Question 0 - Markdown warmup

# This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# >Question 0 is about Markdown.
#
# The next question is about the **Fibonnaci sequence**, *Fn=Fn−2+Fn−1*. In part **a** we will define a Python function `.fib_rec()`
# Below is a …
# ### Level 3 Header
# Next, we can make a bulleted list:
# * Item 1
#     - detail 1
#     - detail 2
# * Item 2
#
# Finally, we can make an enumerated list:
# 1. Item 1
# 2. Item 2
# 3. Item 3
#

# # Question 1 - Fibonnaci Sequence

# a.Write a recursive function fib_rec() that takes input n, a=0, and b=1 and returns the value of Fn for F_0 = a, and F_1 = b.

def fib_rec(n):
    a,b = 0,1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib_rec(n-2)+fib_rec(n-1)   


(fib_rec(7) == 13)and(fib_rec(11) == 89)and(fib_rec(13) == 233)


# b.Write a function fib_for() with the same signature that computes Fn by summation using a for loop.

def fib_for(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a


(fib_for(7) == 13)and(fib_for(11) == 89)and(fib_for(13) == 233)


# c.Write a function fib_whl() with the same signature that computes Fn by summation using a while loop.

def fib_whl(n):
    a,b = 0,1
    i = 1
    while i <= n:
        a,b = b,a+b
        i = i+1
    return a


(fib_whl(7) == 13)and(fib_whl(11) == 89)and(fib_whl(13) == 233)

# d. Write a function fib_rnd() with the same signature that computes Fn using the rounding method.

import math
def fib_rnd(n):
    r = (1+math.sqrt(5))/2
    return round(r**n/math.sqrt(5))


(fib_rnd(7)==13)and(fib_rnd(11)==89)and(fib_rnd(13)==233)

# e. Write a function fib_flr() with the same signature that computes Fn using the truncation method

import math
def fib_flr(n):
    r = (1+math.sqrt(5))/2
    return math.floor(r**n/math.sqrt(5)+1/2)


(fib_flr(7) == 13)and(fib_flr(11) == 89)and(fib_flr(13) == 233)

# +
from pandas import DataFrame
import time
import numpy as np

lis = [10,20,30]

# get the median computation time of fuction rec_time
def rec_time(n):
    tm = []
    for i in range(30):
        start = time.time()
        fib_rec(n)
        end = time.time()
        tm.append(end-start)
        return(np.median(tm))

# get the median computation time of fuction for_time
def for_time(n):
    tm = []
    for i in range(30):
        start = time.time()
        fib_for(n)
        end = time.time()
        tm.append(end-start)
        return(np.median(tm))

# get the median computation time of fuction whl_time
def whl_time(n):
    tm = []
    for i in range(30):
        start = time.time()
        fib_whl(n)
        end = time.time()
        tm.append(end-start)
        return(np.median(tm))
    
# get the median computation time of fuction rnd_time
def rnd_time(n):
    tm = []
    for i in range(30):
        start = time.time()
        fib_rnd(n)
        end = time.time()
        tm.append(end-start)
        return(np.median(tm))

# get the median computation time of fuction flr_time
def flr_time(n):
    tm = []
    for i in range(30):
        start = time.time()
        fib_flr(n)
        end = time.time()
        tm.append(end-start)
        return(np.median(tm))

data = {'fib_rec': [rec_time(lis[0]),rec_time(lis[1]),rec_time(lis[2])],
        'fib_for': [for_time(lis[0]),for_time(lis[1]),for_time(lis[2])],
        'fib_whl': [whl_time(lis[0]),whl_time(lis[1]),whl_time(lis[2])],
        'fib_rnd': [rnd_time(lis[0]),rnd_time(lis[1]),rnd_time(lis[2])],
        'fib_flr': [flr_time(lis[0]),flr_time(lis[1]),flr_time(lis[2])]}
frame = DataFrame(data, index = lis)
# -

frame


# # Question2- Pascal’s Triangle

def triangle_row(n):
    a = 1
    lis = [a]
    for i in range(n):
        i = i+1
        a = int(a*(n+1-i)/i)
        lis.append(a)
    return lis


triangle_row(5)


def triangle(n):
    i = 0
    #get the length of the maximum item in the tiangle
    if n % 2 == 0:
        max_item = triangle_row(n)[int(n/2)]
    else:
        max_item = triangle_row(n)[int((n+1)/2)]
    max_length = len(str(max_item))
    
    while i<= n:
        list = triangle_row(i)
        string = ''
        j = 0
        while j<len(list):
            if j == 0:
                string = str(list[j]).center(max_length)
            else:
                string = string + ' ' + str(list[j]).center(max_length)
            j = j+1 
            
        print(string.center((max_length+2)*n)) #adjust the overall position of the triangle 
        i=i+1


triangle(15)

# # Question 3 - Statistics 101 

import numpy as np
import scipy.stats as st
import math


# a.return a point and interval estimate for the mean based on Normal theory

def norm_est(data,inp,level):
    x_bar,se_x = data.mean(),data.std()  #get the mean and standard error
    z = st.norm.ppf((1+level)/2)  #get Gaussian multiplier
    lwr = x_bar-se_x*z
    upr = x_bar+se_x*z
    level = str(level*100)+"%"
    if inp=="None":
        return {"est":x_bar , "lwr":lwr , "upr":upr , "level":level }
    else:
        return str(round(x_bar,4)) + "[" + str(level*100) + "%" + "CI:" + "(" + str(round(x_bar-se_x*z,4)) + "," + str(round(x_bar+se_x*z,4)) + ")]"


# b.compute a confidence interval based on Binomial experiment

def bino_est(data,method,level,inp):
    x = sum(data==1)
    n=data.size
    p_hat=x/n
    alpha = 1 - level
    
    #1
    if method == "Normal":
        z = st.norm.ppf((1+level)/2)
        lwr = p_hat - z * math.sqrt(p_hat*(1-p_hat)/n)
        upr = p_hat + z * math.sqrt(p_hat*(1-p_hat)/n)
        level = str(level*100)+"%"
        condition = min(n*p_hat,n*(1-p_hat))
        if condition <= 12:
            print("The approximation is not adequate!")
        if inp=="None":
            return {"est":p_hat , "lwr":lwr , "upr":upr , "level":str(level*100) + "%"}
        else:
            return str(p_hat) + "[" + str(level*100) + "%" + "CI:" + "(" + str(lwr) + "," + str(upr) + ")]"
        
    #2
    elif method =="Beta":
        lwr = st.beta.ppf(alpha/2, x, n-x+1)
        upr = st.beta.ppf(1-alpha/2, x+1, n-x)
        if inp=="None" :
            return {"est":p_hat , "lwr":lwr , "upr":upr , "level":str(level*100) + "%" }
        else:
            return str(p_hat) + "[" + str(level*100) + "%" + "CI:" + "(" + str(lwr) + "," + str(upr) + ")]"
        
    #3
    elif method =="Jeff":
        lwr = max(0, st.beta.ppf(alpha/2, x+0.5, n-x+0.5))
        upr = min(1, st.beta.ppf(1-alpha/2, x+0.5,n-x+0.5))
        if inp=="None" :
            return {"est":p_hat , "lwr":lwr , "upr":upr , "level":str(level*100) + "%" }
        else:
            return str(p_hat) + "[" + str(level*100) + "%" + "CI:" + "(" + str(lwr) + "," + str(upr) + ")]"
    
    #4
    elif method =="AC":
        z = st.norm.ppf((1+level)/2)
        n_wave = n + z**2
        p_wave = (x + (z**2)/2)/n_wave
        lwr = p_wave - z * math.sqrt(p_wave*(1-p_wave)/n)
        upr = p_wave + z * math.sqrt(p_wave*(1-p_wave)/n)
        if inp=="None" :
            return {"est":p_wave , "lwr":lwr , "upr":upr , "level":str(level*100) + "%" }
        else:
            return str(p_wave) + "[" + str(level*100) + "%" + "CI:" + "(" + str(lwr) + "," + str(upr) + ")]"
    


# c.creat array and compare methods

# +
import pandas as pd
from pandas import DataFrame

a=[0 for x in range(42)]
b=[1 for y in range(48)]
z=np.array(a+b)

for level in [0.90,0.95,0.99]: #
    print("For level of",level) 
    est = round(norm_est(z,"None",level).get("est"),4)
    lwr = round(norm_est(z,"None",level).get("lwr"),4)
    upr = round(norm_est(z,"None",level).get("upr"),4)
    a_length = upr-lwr
    a_interval=str(est) + "[" + str(level*100) + "%" + "CI:" + "(" + str(lwr) + "," + str(upr) + ")]"
    
    b_length = np.array([-0.1,-0.1,0,0])
    name = np.array(["Normal","Clopper-Pearson","Jeffrey","Agresti-Coull"])
    i = 0
    b_interval=[]
    for method in ["Normal","Beta","Jeff","AC"]:
        est = round(bino_est(z,method,level,"None").get("est"),4)
        lwr = round(bino_est(z,method,level,"None").get("lwr"),4)
        upr = round(bino_est(z,method,level,"None").get("upr"),4)
        b_length[i] = upr - lwr
        b_interval.append(str(est) + "[" + str(level*100) + "%" + "CI:" + "(" + str(lwr) + "," + str(upr) + ")]")
        i = i + 1
    
    #show data via a table
    method_lis=['a. Nomal theory','b. Normal method','b. Beta method','b. Jeff method','b.AC method']
    data = [a_interval,b_interval[0],b_interval[1],b_interval[2],b_interval[3]]
    df = pd.DataFrame(data, index = method_lis, columns=['confidence interval'])
    print(df)
    
    #compare the length of interval produced by each method
    min_int = round(min(a_length , b_length.min()),4) 
    if min_int == a_length:
        print("Normal approximation method produces the interval with the smallest width, which is",min_int)
    else:
        print(name[np.argmin(b_length)],"method produces the interval with the smallest width, which is",min_int)

# -


