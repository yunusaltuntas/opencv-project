"""
Created on Sat Feb 16 23:12:53 2019

@author: yunus
"""
import cv2 as cv
import numpy as np
def nothing(x):
    pass
img=cv.imread("C:/Users/yunus/Desktop/indir.jpg")
img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.namedWindow('image')
cv.createTrackbar('aralik','image',0,255,nothing)
aralik=cv.getTrackbarPos('aralik','image')
cv.createTrackbar('R','image',0,(255-aralik),nothing)
cv.createTrackbar('G','image',0,(255-aralik),nothing)
cv.createTrackbar('B','image',0,(255-aralik),nothing)
swich='0:OFF \n1 : ON'
cv.createTrackbar(swich,'image',0,1,nothing)
while (1):
    aralik=cv.getTrackbarPos('aralik','image')
    r=cv.getTrackbarPos('R','image')
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    s=cv.getTrackbarPos(swich,'image')
    low=np.array([r,g,b])
    high=np.array([(r+aralik),(g+aralik),(b+aralik)])
    mask=cv.inRange(img,low,high)
    mask=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('images',mask)
    k=cv.waitKey(1)&0XFF
    if k==27:
        break
    
