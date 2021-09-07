# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:10:42 2020

@author: User
"""


import cv2
import numpy as np
import math

contours_num=[]
cap = cv2.VideoCapture('6mm.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(history=600,
                                          varThreshold=16,
                                          detectShadows=False)
kernel = np.ones((5,5),np.uint8) 
scale = 0.08
stamp = 1
ave_dis = []
data = open('1234.txt', mode='w')  
k=0
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, 60.0, (960, 540))
while (cap.isOpened()):
    ret, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    
   


    if ret:        
        a = fgbg.apply(frame)
        fgmask = fgbg.apply(frame)
       
        fgmask = cv2.GaussianBlur(fgmask,(5,5),0) #GaussianBlue
        ret,fgmask = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY, np.ones((11,11),np.uint8))
        
          #影像型態open處理
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        #fgmask = cv2.erode(fgmask, np.ones((5,5),np.uint8),iterations = 1)
        #fgmask =  cv2.dilate(fgmask,kernel,iterations = 1)
        #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, np.ones((5,5),np.uint8))
        test = fgmask
        width = cap.get(3)
        height = cap.get(4)
        fps = cap.get(5)
        frames_number = cap.get(7)
        
       
       
        
        
        
        
        #獲得真實ant的影像
        ant = cv2.bitwise_and(frame, frame, mask = fgmask)

        #inverse車輛的遮罩
        fgmask_inv = cv2.bitwise_not(fgmask)
        #fgmask_inv = cv2.erode(fgmask, kernel, iterations = 1)
        
         #用白色當背景
        white=frame.copy()
        white[:,:]=255
        
         #白色背景減去車輛遮罩，變成黑色車子在白色背景移動
        frame_withoutAnt = cv2.bitwise_and(white,white,mask = fgmask_inv)
        #frame_withoutAnt = cv2.erode(frame_withoutAnt,np.ones((5,5),np.uint8),iterations = 1)
        #frame_withoutAnt =  cv2.dilate(frame_withoutAnt,np.ones((8,8),np.uint8),iterations = 500)
        #frame_withoutAnt = cv2.morphologyEx(frame_withoutAnt, cv2.MORPH_CLOSE, np.ones((3,3),np.uint8))

        #[黑色車子在白色背景]+[真實車輛的影像]
        whiteframe_Ant = cv2.add(frame_withoutAnt, ant)

        #取得車子的輪廓
        contours, hierarchy = cv2.findContours(fgmask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #用線在車子輪廓上描出外框
        ant_contour1=frame.copy()
        ant_contour1 = cv2.drawContours(ant_contour1, contours, -1, (0,0,255), 2)


        ant_contour2=frame.copy()
        ant_contour3=frame.copy()
        ant_contour4=frame.copy()


        ant1=frame.copy()
        
        '''z = frame_withoutAnt.reshape((-1, 3))
        z = np.float32(z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 2
        ret,label,center=cv2.kmeans(z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((frame_withoutAnt.shape))
        cv2.imshow('res2',res2)'''

     


        O_x = 540
        O_y = 585
        dis_total = 0         
            
        for i in range(len(contours)):
            cnt = contours[i]
            M = cv2.moments(cnt)
            
            if M["m00"] == 0 or M["m00"]== 0:
                break
            
            
            contours_num.append(len(contours))
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            Cx = int(M["m10"] / M["m00"])
            Cy = int(M["m01"] / M["m00"])
            
            dis = math.sqrt((Cx-540)**2+(585-Cy)**2)
            #cv2.line(ant_contour1, (371, 540), (Cx, Cy), (255, 255, 255), 2)
            dis_total = dis + dis_total
            
            
            '''x,y,w,h = cv2.boundingRect(cnt) #方形
            epsilon = 0.00001*cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,epsilon,True)
            car_contour2 = cv2.drawContours(ant_contour2, [approx], -1, (255,0,0), 2)
            '''
   
            
            
            
            

        
        if len(contours) != 0:    
            ave_dis.append(dis_total/len(contours))
            print(ave_dis[-1], file = data)
        else:
            print(0, file = data)
                    
        cv2.imshow('test', test)
        #cv2.imshow('frame_withoutAnt', frame_withoutAnt)
        #cv2.imshow('frame', frame)
        #cv2.imshow('frame_white',whiteframe_Ant)
        #cv2.imshow('fgmask',fgmask)
        #cv2.imshow('ant',ant)
        cv2.imshow('car_contour1',ant_contour1)
        #cv2.imshow('car_contour2',ant_contour2)
        #cv2.imshow('car_contour3',ant_contour3)
        #cv2.imshow('car_contour4',ant_contour4)
        #cv2.imwrite("road.png",ant_contour3)                  
        #cv2.imwrite("road"+str(stamp)+".png",car_contour3) 
        #cv2.imshow('ant_contour4',ant_contour4)
        #cv2.imshow('a',a) 
        out.write(ant_contour1)
        if cv2.waitKey(1) & 0xFF == ord('q'):                
            break
        
        stamp += 1 
    
       
        
          
    else:
        break
    
    
    

cap.release()
cv2.destroyAllWindows()
data.close()
print( 'width:', width, '\n'+ 'height:', height, '\n'+ 'fps:', fps,'\n'+ 'frames:', frames_number)
print(sum(contours_num))