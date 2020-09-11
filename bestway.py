# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:46:46 2019

@author: Christopher
"""
import numpy as np
import timeit
in_yards=[10,100]
def comp():
    in_meters_comp = [y / 1.1 for y in in_yards]

loop_time=timeit.timeit('comp()',
                        'from __main__ import comp',
                        number=2000)

in_yardsnp=np.array(in_yards)
def np():
    in_meters_np = in_yardsnp / 1.1

np_time=timeit.timeit('np()',
                        'from __main__ import np',
                        number=2000)


def to_meters(y):
    return y / 1.1
in_yards=[10,100]
in_meters_func = map(to_meters, in_yards)

func_time=timeit.timeit('in_meters_func',
                        'from __main__ import in_meters_func',
                        number=2000)



in_yards=[10,100]
for x in range(1000):
    in_yards.append(100)
def comp():
    in_meters_comp = [y / 1.1 for y in in_yards]

loop_time2=timeit.timeit('comp()',
                        'from __main__ import comp',
                        number=2000)


def np():
    in_meters_np = in_yardsnp / 1.1

np_time2=timeit.timeit('np()',
                        'from __main__ import np',
                        number=2000)


def to_meters(y):
    return y / 1.1
in_yards=[10,100]
in_meters_func = map(to_meters, in_yards)

func_time2=timeit.timeit('in_meters_func',
                        'from __main__ import in_meters_func',
                        number=2000)

'''
FuncTime1=1.98
FuncTime2=1.98

LoopTime1=.0006
Looptime2=.108

NPTime1=.0019
NpTime2=.0019

Even when dealing with large lists, Numpy is much more efficient as we
can see by the timeit function. LoopTime increases with list size.
FuncTime does not increase, but it is orders of magnitude slower at all values.



'''


