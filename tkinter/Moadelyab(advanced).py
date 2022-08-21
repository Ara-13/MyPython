# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 01:11:26 2021

@author: Arash
"""

from xlwt import Workbook
wb = Workbook()
Sh1 = wb.add_sheet('Sh1')
Sh1.write(0, 0, 'Payani')
Sh1.write(0, 1, 'Mostamar')
Sh1.write(0, 2, 'Vahed')
Sh1.write(0, 3, 'Moadel')


list_all_moadel = []
list_moadel = []
list_payani = []
list_mostamar = []
list_vahed = []

def m1():
    p = input('payani: ')
    m = input('mostamar: ')
    v = int(input('vahed: '))

    try:
        p = int(p)
    except ValueError:
        p = float(p)
    if m == '':
        one = p
        kol = p*v
        m = 'No Score'
    else:
        try:
            m = int(m)
        except ValueError:
            m = float(m)
        else:
            one = (p*2 + m)/3
            kol = ((p*2 + m)/3)*v

    list_all_moadel.append(kol)
    list_moadel.append(one)
    list_payani.append(p)
    list_mostamar.append(m)
    list_vahed.append(v)

n_times = int(input('Tedad Dars: '))
for i in range(1, n_times+1):
    print(f'\n{i}:')
    m1()

list_vahed_copy = list_vahed.copy()
for x in range(1, n_times+1):
    Sh1.write(x, 0, list_payani.pop(0))
    Sh1.write(x, 1, list_mostamar.pop(0))
    Sh1.write(x, 2, list_vahed.pop(0))
    Sh1.write(x, 3, list_moadel.pop(0))

Sh1.write(x+1, 3, sum(list_all_moadel)/sum(list_vahed_copy))

wb.save('Karname.xls')