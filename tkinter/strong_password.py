# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:00:14 2020

@author: Arash
"""


import random

random_maker1 = []
random_maker2 = []
random_maker3 = []
random_maker4 = []

small_alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
                  'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'w', 'x',
                  'y', 'z']

big_alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(3):
    random_maker1.append(small_alphabet[random.randint(0, 25)])

for j in range(3):
    random_maker2.append(big_alphabet[random.randint(0, 25)])

for k in range(2):
    random_maker3.append(numbers[random.randint(0, 8)])

for M in range(2):
    random_maker4.append(numbers[random.randint(0, 8)])

list_numbers1 = list(random_maker3)
list_numbers2 = list(random_maker4)

mixtures = random_maker1 + list_numbers1 + random_maker2 + list_numbers2

list_mixtures = list(mixtures)

strong_password = ''.join(list_mixtures)

address = 'G:\python.projects\دلخواه\data1.txt'
with open(address, 'a') as file:
    file.write('\n')
    file.write(str(strong_password))
    