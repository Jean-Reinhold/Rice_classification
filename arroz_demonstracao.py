import cv2 as cv 
import numpy as np 

imagem_original = cv.imread( "arroz_casca.jpeg", 0 )
imagem_original = cv.resize( imagem_original, (480, 640) )
imagem_filtrada = cv.GaussianBlur( imagem_original, (9, 9), cv.BORDER_DEFAULT )

imagem_binarizada = cv.adaptiveThreshold( imagem_filtrada ,255 ,cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
            cv.THRESH_BINARY, 11, 2 )

imagem_binarizada = 255 - imagem_binarizada
kernel = np.ones( (5, 5), np.uint8 )

imagem_aberta = cv.morphologyEx( imagem_binarizada, cv.MORPH_CLOSE, kernel )
imagem_dilatada = cv.dilate( imagem_aberta , kernel, iterations = 2)

threshold = 100
canny_output = cv.Canny( imagem_dilatada, threshold, threshold * 2)

contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in contours:
    x, y, w, h = cv.boundingRect(c)
    area = cv.contourArea(c)
    print(area)
   
    cv.rectangle(imagem_original, (x, y), (x+w, y+h), (0, 255, 0), 2)
    




cv.imshow( "Original", imagem_original )
cv.imshow( "Binarizada" , imagem_binarizada )
cv.imshow( "Dilatada", imagem_dilatada )
cv.imshow( "Aberta", imagem_aberta )
cv.imshow( "Canny", canny_output)
cv.waitKey( 0 )