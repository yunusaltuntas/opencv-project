"""
Created on Thu Feb 28 20:52:07 2019
"""
import time
import numpy as np
import cv2 as cv
cap = cv.VideoCapture("C:/Users/yunus/Downloads/Video/highway1.mp4")
feature_params = dict( maxCorners = 10,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
lk_params = dict( winSize  = (5,5),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 50, 0.03))
color = np.random.randint(0,255,(100,3))
ret, old_frame = cap.read()
old_frame=old_frame[230:500,400:600,:]
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

gecis_kontrol=np.zeros(100,(bool))
gecis_zamani=np.zeros(100,np.float)
zaman=np.zeros(100,np.float)
birinciy=np.uint()
birincis=np.uint()
arac_varmi=1000
while(1):
    mask = np.zeros_like(old_frame)
    ret,frame = cap.read()
    frame=frame[230:500,400:600,:]
    if ret==False:
        break
    pts=np.array([[45,100],[130,100],[110,150],[0,150]],np.int32)
    pts=pts.reshape((-1,1,2))
    cv.polylines(frame,[pts],True,(0,255,0))
    cv.line(frame,(0,150),(80,150),(0,255,0),5)
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        if (arac_varmi==1000):
            print("arac yok")
        elif (arac_varmi==i):
            print("arcı inceliyor")
        else:
            continue
        print(i)
        a,b = new.ravel()
        c,d = old.ravel()
        if (45<p1[i,0,0] and 130>p1[i,0,0]):
            if (p1[i,0,1]<150 and 100<p1[i,0,1]):
                if gecis_kontrol[1]==0:
                    gecis_kontrol[1]=True
                    gecis_zamani[1]= (time.time())*1000
                    print(i,"nesne girdi,zamanı:",gecis_zamani[1])
                    arac_varmi=i
        #gecis_zamani[1]= gecis_zamani[1]+1
        if (gecis_kontrol[1]==True):
            if(p1[i,0,1]<200 and p1[i,0,1]>150 and 0<p1[i,0,0] and 80>p1[i,0,0]):
                asd=(time.time())*1000
                gecis_kontrol[1]=0
                arac_varmi=1000
                zaman[i]=asd-gecis_zamani[1]
                if(zaman[i]>500 and zaman[i]<50000):#arçların yakalanılamadıgı zamanlar
                    continue
                birincis=np.float64(14440.43321/zaman[i]) #yesil cizgi ile belirledigim iki kesik serit arasindaki uzaklik 4m alindigi icin v=x/t formulunden gelir
                print("nesne hızı",birincis)
                print(i,"nesnenin zamanı",asd)        
        #frame = cv.line(frame, (a,b),(c,d), color[i].tolist(), 5)
    print(birincis)
    cv.putText(frame,np.str(birincis),(45,100),(cv.FONT_HERSHEY_SIMPLEX),2,(0,0,255),2,(cv.LINE_AA))
    cv.imshow('frame',frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    old_gray = frame_gray.copy()
    old_frame=old_frame[230:500,400:600,:]
    p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
cv.destroyAllWindows()
cap.release()      