# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:25:54 2021

@author: Arash
"""


x = input('number: ')

list_x = []
list_all = []

prime = []
not_prime = [1]

try:
    x = int(x)
except ValueError:
    print('Just "int"')
else:
    for i in range(2, x+1):
        list_all.append(i)
        
    for i in range(2, x+1):
        one = list_all.pop(0)
        for i in range(2, one+1):
            h = one/i
            if h == int(h):
                list_x.append(int(h))
                break
            
        if list_x[-1] == 1:
            prime.append(one)
        else:
            not_prime.append(one)
        list_x = []
        
print(f'\nprime numbers = {prime}')
print(f'not prime numbers = {not_prime}')            