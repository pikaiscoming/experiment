# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:28:34 2020

@author: 皮皮卡卡
"""
for i in range(10000):
    t.append(t0)
    
    t0 = t0 + dt
    
    Q1 = Q0
    k1 = (C*Vp - Q1)/R*C


    Q2 = Q0 + k1 * dt / 2
    k2 = (C*Vp - Q2)/R*C

    Q3 = Q0 + k2 * dt / 2
    k3 = (C*Vp - Q3)/R*C

    Q4 = Q0 + k3 * dt
    k4 = (C*Vp - Q4)/R*C

    Q0 = Q0 + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
    
l1,=plt.plot(t,vc,label='Vc')
l2,=plt.plot(t,vr,label='Vr')
l3,=plt.plot(t,V,label='Vr+Vc')
plt.xlabel("time (s)")
plt.ylabel("V")
plt.legend(handles=[l1,l2,l3],loc='best')
plt.show()