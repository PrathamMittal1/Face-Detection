import cv2
def text(img,msg):
    cv2.putText(img,msg,
                (30,20),cv2.FONT_HERSHEY_PLAIN,2,(25,25,25),2)

def init_info():
    print('''Face and Eyes recognition script; version: 1
          Created by Pratham Mittal; dated: 06 July 2022
          Email me at \"pratham9897521595@gmail.com\"''')

