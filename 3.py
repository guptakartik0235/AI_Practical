#Program to Display an Image
#Enter any Image Path at line 5 within double inverted commas
#Requirements -  opencv-python or cv2 module installed
import cv2
path = "C:/Users/ANAND/Desktop/TEXT DETECTION NUERAL NETWORKS/Ai_Practical/lambo.jpg"
Img = cv2.imread(path)


cv2.imshow("Images",Img)
cv2.waitKey(0)
#Results - Display selected Image 

