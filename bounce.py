# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:31:37 2019

@author: Christopher
"""

def simulate_bounce(coeff,height0,heightend):
    height0*=100
    nextheight=True
    distance=0
    bounce=1
    distance+=height0
    while height0*coeff>=heightend:
        bounce+=1
        distance+=(2*height0*coeff)
        height0=height0*coeff
    
    
    return bounce,distance/100
        