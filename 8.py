#Program to Resize an Image
#Enter any Image Path at line 7 within double inverted commas
#Requirements -  opencv-python or cv2 module installed
#You can Change the x & y values to change image rezising size. 

import cv2
path = "Query.png"

x = int(input("x = "))
y = int(input("y = "))

Img = cv2.imread(path)

ResizedImg = cv2.resize(Img,(x,y))

cv2.imshow("Image",ResizedImg)
cv2.waitKey(0)

#Results - Converts Image to resized Image of Your need 
