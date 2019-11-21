"""
Created on Sun Feb 17 15:41:12 2019
"""
import numpy as np
import cv2 as cv
cap =cv.VideoCapture("C:/Users/yunus/Downloads/Video/highway.mp4")
kernel=np.uint8([[0,-1,0],[-1,5,-1],[0,-1,0]])
sayiiki=0
ilerlemeiki=0
sayibir=0
ilerlemebir=0
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))
fgbg=cv.createBackgroundSubtractorMOG2()
while (True):
    ret,frame=cap.read()
    if ret== False :
        break
    fgmask=fgbg.apply(frame)
    fgmask=cv.morphologyEx(fgmask,cv.MORPH_CLOSE,kernel)
    fgmask=cv.morphologyEx(fgmask,cv.MORPH_OPEN,kernel)
    ret,fgmask=cv.threshold(fgmask,220,255,cv.THRESH_BINARY)
    cv.line(frame,(360,600),(500,600),(0,0,255),2)
    cv.line(frame,(170,600),(350,600),(0,0,255),2)
    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    im2,contour,hierarchy=cv.findContours(fgmask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    if (ilerlemeiki>0):
                  ilerlemeiki=ilerlemeiki-1
    if (ilerlemebir>0):
                  ilerlemebir=ilerlemebir-1
    for i in range(len(contour)):
      cnt=contour[i]
      a,b,x,y=cv.boundingRect(cnt)
      x=np.int(x/2)
      y=np.int(y/2)
      alan=cv.contourArea(cnt)
      yaziiki=np.str(sayiiki)
      cv.putText(frame,yaziiki,(420,500),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv.LINE_AA)
      yazibir=np.str(sayibir)
      cv.putText(frame,yazibir,(280,500),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv.LINE_AA)
      if(alan>7000):
          cv.rectangle(frame,(cnt[-1,0,0],cnt[0,0,-1]),(cnt[-1,0,0]-x,cnt[0,0,-1]+y),(0,0,255),2)
          
          if ((cnt[-1,0,0]>330 and cnt[-1,0,0]<550) and (cnt[0,0,-1]>500 and cnt[0,0,-1]<550)):
              if (ilerlemeiki==0):
                  print(i+1,"inci cisim:",cnt[-1,0,0],cnt[0,0,-1])
                  ilerlemeiki=np.int(y/10)
                  sayiiki=sayiiki+1
          
          if ((cnt[-1,0,0]>120 and cnt[-1,0,0]<330) and (cnt[0,0,-1]>500 and cnt[0,0,-1]<530)):
              if (ilerlemebir==0):
                  print(i+1,"inci cisim:",cnt[-1,0,0],cnt[0,0,-1])
                  ilerlemebir=np.int(y/10)
                  sayibir=sayibir+1
                  
              
    
    #fgmask=cv.bitwise_and(frame,frame,fgmask=fgmask)
    cv.imshow("frame",fgmask)
    cv.imshow("frame1",frame)
    k=cv.waitKey(30)&0xff
    if k==27:
        break
cap.release()
cv.destroyAllWindows()