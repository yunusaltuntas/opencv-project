 # -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:45:14 2019

@author: yunus
"""
import cv2
import cv2 as cv
import numpy as np
MIN_MATCH_COUNT=30

detector=cv2.xfeatures2d.SIFT_create()

FLANN_INDEX_KDITREE=0
flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
flann=cv2.FlannBasedMatcher(flannParam,{})

ilk_x=[]
ilk_y=[]
son_x=[]
son_y=[]
basili_tutma=[]
basili_tutma.append(0)
son_durum=[]
son_durum.append(0)
ilk_kayıt=[]
ilk_kayıt.append(0)
reset=[]
reset.append(0)
karecizmebaslangic=[]
karecizmebaslangic.append(0)
def maus_konumu(event,x,y,flags,param):
    if basili_tutma[-1]==1:
        son_x.append(x)
        son_y.append(y)
        karecizmebaslangic.append(1)
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
        karecizmebaslangic.append(0)
    if event==cv.EVENT_RBUTTONDOWN:
        reset.append(1)

#trainImg=cv2.imread("C:/Users/yunus/Desktop/deneme1.jpg") #burası takip edilecek nesne resmi
#trainImg=cv2.cvtColor(trainImg,cv2.COLOR_BGR2GRAY)
#trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

cv.namedWindow('image',cv.WINDOW_GUI_NORMAL)
cv.setMouseCallback('image',maus_konumu)

cam=cv2.VideoCapture(0)
while True:
    ret, QueryImgBGR=cam.read()
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    if reset[-1]==1:
        trainImg=0
        son_durum.append(0)
        ilk_kayıt.append(0)
        reset.append(0)
        karecizmebaslangic.append(0)
    if karecizmebaslangic[-1]==1:
        cv.rectangle(QueryImgBGR,(ilk_x[-1],ilk_y[-1]),(son_x[-1],son_y[-1]),(0,0,255),2)
    if son_durum[-1]==1:
        if ilk_kayıt[-1]==0:
            trainImg=QueryImg[(ilk_y[-1]+2):(son_y[-1]-2),(ilk_x[-1]+2):(son_x[-1]-2)]
            trainKP,trainDesc=detector.detectAndCompute(trainImg,None)
            ilk_kayıt.append(1)
        queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
        matches=flann.knnMatch(queryDesc,trainDesc,k=2)
        goodMatch=[]
        for m,n in matches:
            if(m.distance<0.75*n.distance):
                goodMatch.append(m)
        if(len(goodMatch)>MIN_MATCH_COUNT):
            tp=[]   
            qp=[]
            for m in goodMatch:
                tp.append(trainKP[m.trainIdx].pt)
                qp.append(queryKP[m.queryIdx].pt)
            tp,qp=np.float32((tp,qp))
            H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
            h,w=trainImg.shape
            trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
            queryBorder=cv2.perspectiveTransform(trainBorder,H)
            cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(0,255,0),5)
        else:
            print ("Not Enough match found- %d/%d"%(len(goodMatch),MIN_MATCH_COUNT))
    cv2.imshow('image',QueryImgBGR)
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()