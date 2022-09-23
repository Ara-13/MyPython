# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:37:26 2021

@author: Arash
"""

print('\nEnter "quit" to quit')

while True:
    x = input('number: ')
    list_x = []
    if x == 'quit':
        break
    try:
        x = int(x)
    except ValueError:
        print('Just "int"')
    else:
        if int(x) == 1:
            print(f'\n{x} is not a prime number')
        else:
            for i in range(2, x+1):
                h = x/i
                if h == int(h):
                    list_x.append(int(h))
                    break
                
            if list_x[-1] == 1:
                print(f'\n{x} is a prime number.')
            else:
                print(f'\n{x} is not a prime number.')
                print(f'{int(h)}*{i} = {x}')
            