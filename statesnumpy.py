# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:12:52 2019

@author: Christopher
"""
import numpy as np
def state_density_rank(filename,rank):
    rank=rank-1
    states=np.loadtxt(filename,delimiter=',',dtype=str)
    area=states[:,2].astype(float)
    pop=states[:,3].astype(float)
    density=np.divide(pop,area)
    g=np.argsort(density)
    states=states[g][::-1]
    return states[rank][0]