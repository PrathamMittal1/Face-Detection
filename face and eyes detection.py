import cv2
import numpy as np
import extra

extra.init_info()
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
first=True
cap=cv2.VideoCapture(0)
ret,img=cap.read()
while ret:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.bilateralFilter(gray,5,1,1)
    
    faces=face_cascade.detectMultiScale(gray)
    if len(faces)>0:
        for (x,y,w,h) in faces:
            img=cv2.circle(img,(x+w//2,y+h//2),(h//2),(0,45,200),2)
            roi_face=gray[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_face)
            if len(eyes)>0:
                extra.text(img,str(len(eyes))+' Eyes detected!')
                for (x2,y2,w2,h2) in eyes:
                    img=cv2.rectangle(img,(x+x2,y+y2),(x+x2+w2,y+y2+h2),(200, 105, 0),1)
            else:
                extra.text(img,'No eyes detected')
    else:
        extra.text(img,'No face detected!')
    
    cv2.imshow('Face and eyes recognition',img)
    k= cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
