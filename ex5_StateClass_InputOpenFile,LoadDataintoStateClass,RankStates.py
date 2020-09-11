# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:51:42 2019

@author: Christopher
"""

class State():
    def __init__(self,name,area,population,abbrev,rank):
        self.name=name
        self.area=area
        self.population=population
        self.abbrev=abbrev
        self.density=0
        self.rank=rank
        
    def pop_density(self):
        self.density=self.population/self.area
        return self.population/self.area
    def __str__(self):
        return self.name
    

def load_us_states(filename):
    states=[]
    with open(filename) as f:
        y=0
        for x in f:
            x=x.strip()
            x=x.split(',')
            name=x[0]
            abbrev=x[1]
            area=float(x[2])
            population=float(x[3])
            states.append(State(name,area,population,abbrev,y))
            states[y].pop_density()
            y+=1
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    sort(states)
    states2=[]
    for x in range(len(states)):
        states2.append(0)
    for x in states:
        states2[x.rank]=x

    return states2


def sort(states):
    for key in states:
        for key2 in states:
            if key.density>key2.density and key.rank>key2.rank:
                temp=key.rank
                key.rank=key2.rank
                key2.rank=temp