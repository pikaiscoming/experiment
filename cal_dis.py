import numpy as np
import matplotlib.pyplot as plt
import os

def dis(x1,x2,y1,y2):
    velocity = np.sqrt((x1-x2)**2+(y1-y2)**2)
    return velocity

write_path = r'd:\Users\皮皮卡卡\Desktop\python'
'''input'''
fig = []

number = []
path = r'd:\Users\皮皮卡卡\Desktop\python\18mm_1'
files = os.listdir(path)
time = [0]*len(files)
we = 1   

for num in files:
    ax = []
    record = {}
    ax2 = []
    instant_velocity_o = []
    instant_velocity = []
    s = path+'\\'+num
    if num[7]=='.':
        order = num[6]
    if num[8]=='.':
        order = num[6]+num[7]
    raw_data = np.loadtxt(s)
    x = np.transpose(raw_data)[0]
    y = np.transpose(raw_data)[1]
    time = range(1, len(x))
    
    
    write = write_path+'\\'+ str(we) + r'.txt'
    data = open(write, mode = 'w')
    
    for i in range(len(y)-1):
        if (317<=x[i]<=397 and 317<=x[i+1]<=397 and 405.5<=y[i]<=540.0 and 405.5<=y[i+1]<=540.0):
            v = dis(x[i],x[i+1],y[i],y[i+1])
            instant_velocity.append(v)
            ax.append(time[i])
            print(time[i], '\t', v, file=data)
        else:
            v = dis(x[i],x[i+1],y[i],y[i+1])
            instant_velocity_o.append(v)
            ax2.append(time[i])
    plt.scatter(ax, instant_velocity,marker='o', s=3, c='r',alpha=0.6)
    plt.xlabel("frames",fontsize=13)
    plt.ylabel("velocity (pixel/s)",fontsize=13)
    plt.grid(b=1, c='k', ls='-.', alpha=0.2)
    
    data.close()
    we=we+1
    

'''print'''

plt.show()
