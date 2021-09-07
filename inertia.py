# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:11:16 2020

@author: 皮皮卡卡
"""
import numpy as np
import matplotlib.pyplot as plt

'''begin petermeter'''
I1 ,I2, I3 = 20, 40, 60
w1i, w2i, w3i = 0, 20, 0.05
time = np.arange(0, 3, 0.0001)
dt = 0.0001
w1f = []
w2f = []
w3f = []
w1f.append(w1i)
w2f.append(w2i)
w3f.append(w3i)



'''simulation'''
def Euler1(w1i,I2):    
    w1 = ((I2-I3)/I1)*w2i*w3i*dt + w1i    
    return w1
def Euler2(w2i,I2):    
    w2 = ((I3-I1)/I2)*w1i*w3i*dt + w2i
    return w2
def Euler3(w3i,I2):    
    w3 = ((I1-I2)/I3)*w1i*w2i*dt + w3i 
    return w3
for i in range(len(time)-16500):
    w1i = Euler1(w1f[-1],40)
    w2i = Euler2(w2f[-1],40)
    w3i = Euler3(w3f[-1],40)
    w1f.append(w1i)
    w2f.append(w2i)
    w3f.append(w3i)
for i in range(len(time)-16500,len(time)-1):
    w1i = Euler1(w1f[-1],10)
    w2i = Euler2(w2f[-1],10)
    w3i = Euler3(w3f[-1],10)
    w1f.append(w1i)
    w2f.append(w2i)
    w3f.append(w3i)
   
plt.figure(figsize=(10,7),dpi=80, facecolor='w', edgecolor='k')
S1 =plt.scatter(time, w1f, s=8,c='b',marker='o',label = '\u03C91',alpha=0.6)
S2 =plt.scatter(time, w2f, s=8,c='r',marker='o',label = '\u03C92',alpha=0.6)
S3 =plt.scatter(time, w3f, s=8,c='g',marker='o',label = '\u03C93',alpha=0.6)
plt.xlabel("Time (s)",fontsize=15)
plt.ylabel("Angle velocity (1/s)",fontsize=15)
plt.legend(handles=[S1,S2,S3],loc='best',fontsize=15)
plt.grid(b=1, c='k', ls='-.', alpha=0.2)
plt.title('\u03C91=0     \u03C92=20     \u03C93=0.05 (1/s)',fontsize=15)
plt.show()
