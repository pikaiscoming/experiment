# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:49:01 2021

@author: 皮皮卡卡
"""
import numpy as np
import matplotlib.pyplot as plt

'''set up parameter'''


d = 998         #density of water
r = 0.001       #radius of bubble 
g = 9.81        #gravity
mu = 0.001      #dynamic viscoity 
req = r         #equivalent radius 
u0 = 0         #initial x-velocity 
w0 = 0         #initial y-velocity
x0 = 0.01       #initial distance between two bubbles 
y0 = 0.0008     #intiial height of bubble  
dt = 0.00001
Vb = 4/3*np.pi*r**3
x = []
y = []
u = []
v = []
t0 = 0
'''define function'''

def Mx (x):
    return 1 + (3/8)*((r/x)**3)

def My (x):
    return 1 + (3/16)*((r/x)**3)

def dMydx (x):
    return -9/8*(req)**3*x**(-4)    

def dMydt (x,u):
    return -9/16*(req**3)*(x**-4)*u

def dMxdt (x,u):
    return -9/8*(req**3)*(x**-4)*u

def Dx (x,u):
    return 24*np.pi*mu*req*u(1+(1/4)*((req/x)**3))
    
def Dy (x,w):
    return 24*np.pi*mu*req*w(1+(1/8)*((req/x)**3))

def y2nd (x,u,w):
    return (2*g-Dy(x, w)/(d*Vb)-dMydt(x,u)*w)/My(x)

def x2nd (x,u,w):
    return ((1/2*((w**2)*dMydx(x)+(u**2)*dMxdt(x,u))-Dx(x,u)-dMxdt(x,u)*u)
            /Mx(x))
    
'''run simulation'''


for i in range(10000):
    h=dt/2
    Q1x = u0 + h*x2nd(x0,u0,w0)            
    Q1y = w0 + h*y2nd(x0,u0,w0)
    K1x = x2nd(x0+u0*h,Q1x,Q1y)    
    K1y = y2nd(x0+h*u0,Q1x,Q1y)
    Q2x = u0 + h*K1x           
    Q2y = w0 + h*K1y
    K2x = x2nd(x0+h*Q1x,Q2x,Q2y)   
    K2y = y2nd(x0+h*Q1x,Q2x,Q2y)
    Q3x = u0 + dt*K2x         
    Q3y = w0 + dt*K2y
    K3x = x2nd(x0+dt*Q2x,Q3x,Q3y)      
    K3y = y2nd(x0+dt*Q2x,Q3x,Q3y)
    '''differential term'''
    
    
    
    
    
    






