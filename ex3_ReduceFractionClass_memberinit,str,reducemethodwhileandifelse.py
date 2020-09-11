# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:57:24 2019

@author: Christopher
"""

class Fraction():
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        
    def __str__(self):
        return '{0:d}/{1:d}'.format(self.numerator,self.denominator)
        
    def reduce(self):
        divisible=True
        
        while divisible==True:
            x=2
            divided=False
            while divided==False:
                
                if self.denominator%x==0 and self.numerator%x==0:
                    self.denominator=self.denominator/x
                    self.numerator=self.numerator/x
                    divided=True
                else:
                    x=x+1
                if x==self.denominator:
                    divided=True
                    divisible=False
        self.denominator=int(self.denominator)
        self.numerator=int(self.numerator)