# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:55:38 2020

@author: 皮皮卡卡
"""

import numpy as np
import matplotlib.pyplot as plt
import openpyxl
'''input'''
raw_data = np.loadtxt(r'd:\Users\皮皮卡卡\Desktop\python\0mm_1_4.txt',delimiter ='\t')

y = np.transpose(raw_data)[1]
x = np.transpose(raw_data)[0]




S1 =plt.scatter(x,-y,s=14,c='b',marker='o',label='exponential decay',alpha=0.6)
plt.xlabel("x",fontsize=13)
plt.ylabel("y",fontsize=13)
plt.grid(b=1, c='k', ls='-.', alpha=0.2)
plt.show()
#plt.savefig('1.png')
path = []



for i in range(len(y)-1):
    dis = np.sqrt((x[i+1]-x[i])**2
                +(y[i+1]-y[i])**2)
    path.append(dis)
'''excel'''
fn = 'experiment.xlsx' # excel
wb = openpyxl.load_workbook(fn) # excel
ws = wb.get_sheet_by_name('work sheet')   # excel
 
print("The Distance from Oil" , np.sqrt((x[0]-373.5)**2+(y[0]-(y[0]-32))**2))
    
print("Path Length" , sum(path))
print("Displacement" , np.sqrt((x[0]-x[-1])**2+(y[0]-y[-1])**2))
ws['I7'] = np.sqrt((x[0]-373.5)**2+(y[0]-(y[0]-32))**2) # excel

wb.save('experiment.xlsx') # excel