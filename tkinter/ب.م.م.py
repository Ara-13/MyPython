# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:34:39 2021

@author: Arash
"""


x = x1 = int(input('adad aval ra vared konid: '))
y = y1 = int(input('adad dovom ra vared konid: '))

list_x1 = []
list_y1 = []

for i1 in range(1, x1+1):
    h1 = x/i1
    if h1 == int(h1):
        list_x1.append(int(h1))

for i2 in range(1, y1+1):
    h2 = y/i2
    if h2 == int(h2):
        list_y1.append(int(h2))

M_M = set(list_x1).intersection(set(list_y1))
result = list(sorted(M_M))

try:
    print((x, y),'=',result[-1])
except IndexError:
    print("It's Impossible!")