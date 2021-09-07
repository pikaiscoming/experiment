# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:55:07 2020

@author: 皮皮卡卡
"""

import openpyxl

mtlist = []
fn = 'xxx.xlsx'
wb = openpyxl.load_workbook(fn) 
ws = wb.get_sheet_by_name('sheet name')

for cell in list(ws.columns)[0]: #get data in excel worksheet
    print(cell.value)
    mtlist.append(cell.value)

for i in range(1785):             #write data into excel
    row1 = [i, i**2]
    ws.append(row1)

wb.save('xxx.xlsx')