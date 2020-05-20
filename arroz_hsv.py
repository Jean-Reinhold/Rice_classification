import cv2 as cv 
import numpy as np 

src = cv.imread("amostra_lcd.jpeg")
src = cv.resize(src, (480, 640))

b, g, r = cv.split(src) 
src = cv.merge((b,g,r))

max_h = 255  
max_s = 255
max_v = 255
min_h = 0
min_s = 0 
min_v = 0


def evento_troca_barra(x):

    global max_h  
    global max_s 
    global max_v 
    global min_h     
    global min_s
    global min_v
  
    max_h = cv.getTrackbarPos("max_h", "Filtro HSV")
    max_s = cv.getTrackbarPos("max_s", "Filtro HSV")
    max_v = cv.getTrackbarPos("max_v", "Filtro HSV")   
    min_h = cv.getTrackbarPos("min_h", "Filtro HSV")
    min_s = cv.getTrackbarPos("min_s", "Filtro HSV")
    min_v = cv.getTrackbarPos("min_v", "Filtro HSV") 
    img = src #cv.cvtColor(src, cv.COLOR_BGR2)
    
    minHSV = np.array([[[min_h, min_s, min_v]]])
    maxHSV = np.array([[[max_h, max_s, max_v]]])
    
    maskHSV = cv.inRange(img, minHSV, maxHSV)
    resultHSV = cv.bitwise_and(src, src, mask = maskHSV)

    
    cv.imshow("Filtro HSV",maskHSV)
 
cv.namedWindow('Filtro HSV')
cv.createTrackbar("max_h", "Filtro HSV", 0, 255, evento_troca_barra)
cv.createTrackbar("min_h", "Filtro HSV", 0, 255, evento_troca_barra)
cv.createTrackbar("max_v", "Filtro HSV", 0, 255, evento_troca_barra)
cv.createTrackbar("min_v", "Filtro HSV", 0, 255, evento_troca_barra)
cv.createTrackbar("max_s", "Filtro HSV", 0, 255, evento_troca_barra)
cv.createTrackbar("min_s", "Filtro HSV", 0, 255, evento_troca_barra)

evento_troca_barra(0)

while (True): 
        k = cv.waitKey(0)
        if k == 27:
            break

