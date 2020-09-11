# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:53:51 2019

@author: Christopher
"""

def states_within_n(filename, state, n):
    #state=[state]
    z=state
    with open(filename) as f:
        f.readline()
        borders=[]
        for x in f:
            x=x.strip()
            x=x.split(',')
            borders.append(x[1].split('-'))
    #return borders
    states=[]
    for x in borders:
        flag=True
        for a in states:
            if x[0]==a:
                flag=False
        if flag==True:
            states.append(x[0])
    for x in borders:
        flag=True
        for a in states:
            if x[1]==a:
                flag=False
        if flag==True:
            states.append(x[1])
    #return states        
    poss=[[[state]]]
    
    if n>0:
        
        count=0
        for x in states:
            a=[x]
            poss.append([[state]])
            poss[count].append(a)
            count+=1
        del poss[len(poss)-1]
        count=0
        for x in poss:
            keep=False
            for y in borders:
                if x==y or x[::-1]==y:
                    keep=True
            if keep==False:
                del poss[count]
                count-=1
            count+=1
            
        return poss
        #for x in states:
         #   poss[count].append(x)
          #  count+=1
        #n=n-1
    #return poss
    
'''    
    for x in states:
        b=[x]
        possibilities.append(b)
    for x in possibilities:
        for y in possibilities:
            possibilities.append(x.append(y))
    return possibilities
    m=n
    while m>0:
        count=0
        for x in possibilities:
            while flag==True:
                flag=True
                for y in states:
                    if y not in x:
                        x.append(y)
                        flag=False
        m=m-1
    return possibilities
'''
'''                
    if n==0:
        return possibilities.append(state)
    else:
        link=
        possibilities.append(link+state[0])
    
    
    
    
    count=0
    bordersstate=[]
    for x in borders:
        if state in x:
            bordersstate.append(x)
    final=[]        
    if n==0:
        for x in final:
            x=x+state
        if len(final)==0:
            final.append(state)
        return final
    else:
        for x in borders:
            final.append(x)
            
            
        return states_within_n(filename,state,n-1)
'''            
'''        
    links=[]
    for x in bordersstate:
        if x[0]==state:
            links.append(x[1])
        if x[1]==state:
            links.append(x[0])
    for x in links:
        for y in bordersstate:
            if x in bordersstate and y in bordersstate:
                x=x+states_within_n(filename,x,n-1)
    
    
    return bordersstate
'''


'''
Solution
import csv

# Some of you may have recognized this as a graph-theory problem
# (all walks of length n from a starting node n). Whether you did or
# didn't, this problem shares the same structure as the permutations
# example from the week 4 slides.


# This function loads the border_data.csv file to the specifications in the lab
def load_borders():
    borders = []
    with open('border_data.csv', 'r') as f:
        for line in csv.reader(f):
            states = line[1].split('-')
            if len(states) == 2:
                borders.append([states[0], states[1]])

    return borders


# Helper function - given a list of states, returns a list of neighboring
# states
def neighbors(borders, states):
    neighbors = list()

    for a_border in borders:
        if a_border[0] in states:
            neighbors.append(a_border[1])
        elif a_border[1] in states:
            neighbors.append(a_border[0])

    return neighbors


# The main event - notice this function calls itself.
def states_within_n(borders, state, n):
    if n == 0:
        return [[state]]

    paths = list()
    for states in states_within_n(borders, state, n-1):
        for neighbor in neighbors(borders, states):
            if neighbor not in states:
                paths.append([neighbor] + states)

    # Remove duplicate paths. You could also experiment with Python sets
    # to do this more efficiently, but the method below uses only loops
    no_dupes = list()
    for a_path in paths:
        if sorted(a_path) not in no_dupes:
            no_dupes.append(sorted(a_path))

    return no_dupes


borders = load_borders()
'''