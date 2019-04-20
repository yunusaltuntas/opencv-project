# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:33:15 2019

@author: yunus
"""
import numpy as np
import cv2 as cv
cap=cv.VideoCapture(0)
ilk_x=[]
ilk_y=[]
son_x=[]
son_y=[]
basili_tutma=[]
basili_tutma.append(0)
son_durum=[]
son_durum.append(0)
def maus_konumu(event,x,y,flags,param):
    if basili_tutma[-1]==1:
        son_x.append(x)
        son_y.append(y)
    if event == cv.EVENT_LBUTTONDOWN:
        if basili_tutma[-1]==0:
            ilk_x.append(x)
            ilk_y.append(y)
            basili_tutma.append(1)
    if event ==cv.EVENT_LBUTTONUP:
        son_x.append(x)
        son_y.append(y)
        basili_tutma.append(0)
        son_durum.append(1)
    if event==cv.EVENT_RBUTTONDBLCLK:
        son_durum.append(0)
        
        
cv.namedWindow('image',cv.WINDOW_GUI_NORMAL)
cv.setMouseCallback('image',maus_konumu)
while(1):
    ret,frame=cap.read()
    if basili_tutma[-1]==1:
        cv.rectangle(frame,(ilk_x[-1],ilk_y[-1]),(son_x[-1],son_y[-1]),(0,0,255),2)
    if son_durum[-1]==1:
        img=frame[(ilk_y[-1]+2):(son_y[-1]-2),(ilk_x[-1]+2):(son_x[-1]-2),:]
        son_durum.append(0)
            
    
    
    
    cv.imshow('image',frame)
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
cv.imshow("frame",img)
cv.waitKey(0)
cv.destroyAllWindows()
cap.release()