# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:53:31 2021

@author: 皮皮卡卡
"""
import numpy as np
import matplotlib.pyplot as plt

def dis(x1,x2,y1,y2):
    velocity = np.sqrt((x1-x2)**2+(y1-y2)**2)
    return 240*velocity*pix

#pix = 0.01505625 #cm per pix 5rom
pix=0.00643356643356643 #cm per oix 10rpm

'''input data'''
raw_data_l = np.loadtxt('hit5_l',delimiter ='\t')
raw_data_r = np.loadtxt('hit5_r',delimiter ='\t')

y_data_l = np.transpose(raw_data_l)[1]
x_data_l = np.transpose(raw_data_l)[0]
y_data_r = np.transpose(raw_data_r)[1]
x_data_r = np.transpose(raw_data_r)[0]

'''calculate'''
v_l=[]
v_r=[]
for i in range(len(x_data_l)-1):
    v_l.append(dis(x_data_l[i], x_data_l[i+1], y_data_l[i], y_data_l[i+1]))
for i in range(len(x_data_r)-1):
    v_r.append(dis(x_data_r[i], x_data_r[i+1], y_data_r[i], y_data_r[i+1]))
    
'''plot'''
frames = range(len(v_l))
frames1= range(len(v_r))
c_l=range(len(y_data_l)-1)
c_r=range(len(y_data_r)-1)

plt.figure(figsize=(10,7),dpi=80, facecolor='w', edgecolor='k')
S1 = plt.scatter(frames, v_l, s=25,c=c_l,cmap='hsv', marker='o',alpha=0.5,label='left bubble')
S2 = plt.scatter(frames1, v_r, s=25, c=c_r,cmap='hsv', marker='o',alpha=0.5,label='right bubble')
plt.grid(b=1, c='k', ls='-.', alpha=0.2)
plt.xlabel("frames",fontsize=13)
plt.ylabel("velocity (cm/s)",fontsize=13)
plt.legend(handles=[S1,S2],loc=2,fontsize=13)
plt.show()

