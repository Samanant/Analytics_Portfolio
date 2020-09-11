# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:41:39 2019

@author: Christopher
"""

#Places new queens, doesn't move existing queens to make room for new ones

import copy
class ChessBoard():
    def __init__(self,size):
        self.size=size
        self.board=[]
        self.row=[]
        self.queens=0
        self.queen_list=[]
        for x in range(size):
            self.row.append('-')
        for x in range(size):
            rows=copy.deepcopy(self.row)
            self.board.append(rows)
        
    def __str__(self):
        return self.board
    def place_queen(self):
        rowcheck=self.queens
        colcheck=0
        while colcheck<self.size:
            check=True
            for x in range(self.size):
                if 'Q' in self.board[x][colcheck]:
                    check=False
                    
            upright=True
            n=1
            while upright==True:
                try:
                    if self.board[rowcheck-n][colcheck+n]=='Q':
                        check=False
                except IndexError:
                    upright=False
                n+=1
            
            upleft=True
            n=1
            while upleft==True:
                try:
                    if self.board[rowcheck-n][colcheck-n]=='Q':
                        check=False
                except IndexError:
                    upleft=False
                n+=1
                
            downright=True
            n=1
            while downright==True:
                try:
                    if self.board[rowcheck+n][colcheck+n]=='Q':
                        check=False
                except IndexError:
                    downright=False
                n+=1
                
            downleft=True
            n=1
            while downleft==True:
                try:
                    if self.board[rowcheck+n][colcheck-n]=='Q':
                        check=False
                except IndexError:
                    downleft=False
                n+=1
            if check==True:
                self.board[colcheck][rowcheck]='Q'
                self.queen_list.append(Queen(rowcheck,colcheck))
                colcheck=self.size
                self.queens+=1
                return True
            else:
                colcheck+=1
        if colcheck==self.size and check==False:
            
            return False
            
class Queen():
    def __init__(self,row,col):
        self.row=row+1
        self.column=col+1
    def __str__(self):
        return 'Q({0}, {1})'.format(self.row,self.column)
    
    
    
'''
Solution
class Queen():

    def advance(self):
        if self.row < self.rows:
            self.row += 1
            return self.find_solution()

        if self.neighbor and not self.neighbor.advance():
            return False

        self.row = 1
        return self.find_solution()

    def can_attack(self, row, column):
        if self.row == row:
            return True

        col_diff = column - self.column
        if self.row + col_diff == row or self.row - col_diff == row:
            return True

        if self.neighbor:
            return self.neighbor.can_attack(row, column)
        else:
            return False

    def find_solution(self):
        while self.neighbor and self.neighbor.can_attack(self.row, self.column):
            if not self.advance():
                return False

        return True

    def __init__(self, column, neighbor, rows):
        self.row = 1
        self.column = column
        self.neighbor = neighbor
        self.rows = rows

    def __str__(self):
        return 'Q({0}, {1})'.format(self.row, self.column)


class ChessBoard():

    def __init__(self, n):
        self.n = n
        self.c = 0
        self.queen_list = []
        self.last_queen = None
        self.has_solution = False

    def place_queen(self):
        self.c += 1
        self.last_queen = Queen(self.c, self.last_queen, self.n)
        self.queen_list.append(self.last_queen)
        if self.last_queen.find_solution():
            self.has_solution = True
        else:
            self.has_solution = False

        return self.has_solution
'''