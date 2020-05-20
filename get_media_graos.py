import cv2 as cv 
import os 
import numpy as np 

def get_channel_media(channel): 
    array = np.array(channel)
    return np.median(array) 

def read_img(path, colorspace): 
    img = cv.imread(path) 
    return cv.cvtColor(img, colorspace)

 
 
gV_paths = os.listdir("graosV/")
gB_paths = os.listdir("graosB/")

i = 0
for path in gB_paths: 
    img = read_img("graosB/" + path, cv.COLOR_BGR2YCR_CB) 
    channels = cv.split(img) 
    medias = []
    
    for channel in channels: 
        medias.append( get_channel_media(channel) ) 
        
    with open("mg_B" + str(i), "w") as document: 
        document.write(' '.join([str(elem) for elem in medias]) ) 
        document.close 
    i += 1
            
        