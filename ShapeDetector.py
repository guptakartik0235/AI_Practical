#This algoritm inputs image with Many shapes
#Enter Your Path at line 37 and you code is Ready to Work u
#Requirements - opencv-Python and Numpy Library

import cv2
import numpy as np

def getContours(img):
    Contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in Contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgContour,cnt,-1,(0,0,255),2)
        perimeter = cv2.arcLength(cnt,True)
        print(perimeter)
        approx = cv2.approxPolyDP(cnt,perimeter*0.02,True)
        print(approx)
        corners  = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(imgContour,(x,y),((x+w),(y+h)),(0,255,0),3)
        if corners==3:
            objectType = "Triangle"
        elif corners==4:
            aspRatio = w/float(h)
            if aspRatio>0.96 and aspRatio<1.1:
                objectType = "square"
            else:
                objectType= "Rectangle"
        elif corners ==5:
            objectType = "Pentagon"
        elif corners == 6:
            objectType = "Hexagon"
        else:
            objectType = "Circle"
        cv2.putText(imgContour,objectType,(x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.7,(100,100,100),3)


path = "Your Path here"
img = cv2.imread(path)
imgContour = img.copy()
GrayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
BlurImg = cv2.GaussianBlur(GrayImg,(7,7),1)

CannyImg = cv2.Canny(BlurImg,50,50)

getContours(CannyImg)

#cv2.imshow("Original",img)
#cv2.imshow("GrayImg",CannyImg)
cv2.imshow("BlurImg",BlurImg)
cv2.imshow("Contour",imgContour)
cv2.waitKey(0)

#Results - It detects various Shapes from Images such as Square,Pentagon,Rectangle,Hexagon & Circle and label them









