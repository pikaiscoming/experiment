# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:26:29 2020

@author: 皮皮卡卡
"""
import numpy as np
import os
 
number = [0]*2671
path = r'd:\Users\皮皮卡卡\Desktop\python\18mm_2'
files = os.listdir(path)
for num in files:

    s = path+'\\'+num
    if num[7]=='.':
        order = num[6]
    if num[8]=='.':
        order = num[6]+num[7]
    raw_data = np.loadtxt(s)
    x = np.transpose(raw_data)[0]
    y = np.transpose(raw_data)[1]

    
    

    data = open(r'd:\Users\皮皮卡卡\Desktop\python\18mm_2_runexit.txt', mode='w') 
    
    for i in range(len(y)):
        if (328.5<=x[i]<=551.0 and 0<=y[i]<=117.5):
            number[i] = number[i] + 1
for a in range(2671):       
    print(a*1/30, '\t', number[a], file=data)
    
data.close()

    



    