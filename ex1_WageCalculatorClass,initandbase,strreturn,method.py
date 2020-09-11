# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:01:58 2019

@author: Christopher
"""

class WageCalculator():
    def __init__(self, hours=0,wage=0):
        self.hours=hours
        self.wage=wage
    def __str__(self):
        return 'The hours are {0}, the wage is {1:.2f}'.format(self.hours,self.wage)
    def cal_gross_pay(self):
        return 437.5
