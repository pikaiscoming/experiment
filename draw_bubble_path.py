# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:25:45 2021

@author: 皮皮卡卡
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

'''load the data of path'''
raw_data_l = np.loadtxt('hit5_l',delimiter ='\t')
raw_data_r = np.loadtxt('hit5_r',delimiter ='\t')

y_data_l = np.transpose(raw_data_l)[1]
x_data_l = np.transpose(raw_data_l)[0]
y_data_r = np.transpose(raw_data_r)[1]
x_data_r = np.transpose(raw_data_r)[0]

'''draw the point on picture'''

pix=0.00643356643356643 #cm per oix 10rpm
#pix = 0.00702702702702703 #cm per pix 5rpm
c_l=range(len(y_data_l))
c_r=range(len(y_data_r))
plt.figure(figsize=(10,7),dpi=80, facecolor='w', edgecolor='k')
plt.scatter(pix*x_data_l, -y_data_l*pix, s=75,c=c_l,cmap='hsv', marker='o',alpha=0.5)
plt.scatter(pix*x_data_r, -y_data_r*pix, s=75, c=c_r,cmap='hsv', marker='o',alpha=0.5)
plt.grid(b=1, c='k', ls='-.', alpha=0.2)
plt.xlabel("x (cm)",fontsize=13)
plt.ylabel("y (cm)",fontsize=13)
cbar = plt.colorbar()
cbar.set_label('frames',fontsize=13)

plt.show()