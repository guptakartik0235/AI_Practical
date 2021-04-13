#Program to Display a Blurred Image
#Enter any Image Path at line 6 within double inverted commas
#Requirements -  opencv-python or cv2 module installed
#You can also change Value of x to any odd numbee according to blur needed
import cv2
path = "Ai_Practical\lambo.jpg"
x = int(input("Value of Blur:- ")) 
Img = cv2.imread(path)
BlurImg = cv2.GaussianBlur(Img,(x,x),7)
cv2.imshow("Image",BlurImg)
cv2.waitKey(0)
#Results - Display selected Image which is Blurred