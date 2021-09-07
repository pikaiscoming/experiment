# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:41:49 2020

@author: 皮皮卡卡
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
'''prepare'''

#Vc/V=1/np.sqrt(1+(2*np.pi*RC*x)**2)
#Vr/V=1/np.sqrt(1+1/(2*np.pi*RC*x)**2)
I=0.000007515
k=0.001368829


'''Theoretical functions''' 

#f=np.linspace(0,50,4000)
#y = 

'''fitting'''

raw_data = np.loadtxt('0616 damping 1 short.txt',delimiter ='\t')

y_data = np.transpose(raw_data)[0]
x_data = np.transpose(raw_data)[1]
transposeangle= np.arccos(np.sqrt(y_data/1.597))-np.arccos(np.sqrt(0.913/1.597))
t=x_data
v=transposeangle
angle=[]
time=[]
for i in range(len(v)):
    if(v[i]>v[i-1] and v[i]>v[i+1]):
        t0=t[i]
        v0=v[i]
        angle.append(v0)
        time.append(t0)

time=np.array(time)
angle = np.degrees(angle)
angle = np.array(angle)
y_data= np.degrees(transposeangle)
raw_data = np.loadtxt('0616 damping 1',delimiter ='\t')

x1_data = np.transpose(raw_data)[0]
y1_data = np.transpose(raw_data)[1]

transposeangle1= np.arccos(np.sqrt(x1_data/1.597))-np.arccos(np.sqrt(0.913/1.597))
x1_data = np.degrees(transposeangle1)
def Gaussion_peak(x,A,a,h):
    return A*np.exp(-a*x)-h
init_fitting = (0.473)
#initialGuess = (99.9882,0.723331)
#best_fitting = (0.00056,0.00016)

popt,pcov = curve_fit(Gaussion_peak,time,angle,maxfev=100000)
perr = np.sqrt(np.diag(pcov))
print(popt)
print(pcov)
print(perr)
dy=perr[0]

'''other fitting function'''



'''print''' 

plt.figure(figsize=(10,7),dpi=80, facecolor='w', edgecolor='k')
S1 =plt.scatter(time,angle,s=14,c='b',marker='o',label='exponential decay',alpha=0.6)
L2,=plt.plot(y1_data,x1_data,c='g',label='Angular displacement',alpha=0.5)
L1,=plt.plot(time,Gaussion_peak(time,*popt),'r--',label='Fitting exponential')
#T1,=plt.plot(f,y,c='r',label='Theoretical value')
#plt.annotate("y=4.32(1-e^((-t)/RC)+h", xy=(6.6,1.5), xytext=(6.6,1.5), fontsize=14)
#plt.annotate("5τ=0.05 (ms)", xy=(3,-1.9), xytext=(3,-1.9), fontsize=13)
#plt.errorbar(time,Gaussion_peak(time,*popt),yerr=dy,fmt='.',ecolor='r', color='g',elinewidth=1,capsize=3)
#plt.yticks(np.arange(0, 5, 1))
#plt.xticks(np.arange(1, 1.0, 0.1))
#plt.axvline(x=5,ls='--')
#plt.axhline(y= ,x0=, x1=, sl='-')
plt.axis([0, 25, 0, 30])


plt.xlabel("Time (s)",fontsize=13)
plt.ylabel("Angle (degree)",fontsize=13)
plt.legend(handles=[L2,S1,L1],loc=1,fontsize=13)
plt.grid(b=1, c='k', ls='-.', alpha=0.2)
plt.show()
#plt.savefig('1.png')

