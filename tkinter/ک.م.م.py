# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:59:07 2021

@author: Arash
"""


x = int(input('adad aval ra vared konid: '))
y = int(input('adad dovom ra vared konid: '))

list_x1 = [x]
list_y1 = [y]

for i1 in range(2, y+1):
    h1 = x*i1
    list_x1.append(h1)

for i2 in range(2, x+1):
    h2 = y*i2
    list_y1.append(h2)

M_M = list(sorted(set(list_x1).intersection(set(list_y1))))

print('[',x,',',y,']','=',M_M[0])