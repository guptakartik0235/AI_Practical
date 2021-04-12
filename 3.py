#Program to Display an Image
#Enter any Image Path at line 5 within double inverted commas
#Requirements -  opencv-python or cv2 module installed
import cv2
path = "Type Your Image Path Here within Double inverted Commas"
Img = cv2.imread(path)
cv2.imshow("Image",Img)
cv2.waitKey(0)
#Results - Display selected Image 

