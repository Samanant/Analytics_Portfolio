# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 19:02:48 2019

@author: Christopher
"""

class HighRoller():
    def __init__(self):
        self.players=[]
        self.numplayers=0
    def __str__(self):
        return ''
    def add_player(self,name):
        name=PairOfDice(name)
        self.players.append(name)
        self.numplayers+=1
    def roll_all(self):
        for x in self.players:
            x.roll()
    def winner(self):
        count=0
        winners=[]
        for x in self.players:
            number=x.total()
            #y=x.total()
            if number>count:
                count=x.total()
        for x in self.players:
            number=x.total()
            if number==count:
                winners.append(x.name)
        return winners
        
        
        
        
        
import random
class PairOfDice():
    def __init__(self, name):
        self.dice1=0
        self.dice2=0
        self.name=name
    def __str__(self):
        return 'The dice show {0}'.format(self.dice1+self.dice2)
    def roll(self):
        self.dice1=random.randint(1,6)
        self.dice2=random.randint(1,6)
    def total(self):
        return self.dice1+self.dice2