# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:46:51 2019

@author: Christopher
"""
import random
class PairOfDice():
    def __init__(self):
        self.dice1=0
        self.dice2=0
    def __str__(self):
        return 'The dice show {0}'.format(self.dice1+self.dice2)
    def roll(self):
        self.dice1=random.randint(1,6)
        self.dice2=random.randint(1,6)
    def total(self):
        return self.dice1+self.dice2


some_dice = PairOfDice () 
count = 0
for i in range(0 , 1000): 
    some_dice.roll() 
    if some_dice.total() == 7: 
        count += 1
print( '# of times you rolled a 7: {} ' . format(count ))
