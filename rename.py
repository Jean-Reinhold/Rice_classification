import os 

i = 0 
path_origem = "graosV/"
name = "v_"
paths = os.listdir(path_origem)

for path in paths: 
    os.rename((path_origem+path), (path_origem+name+str(i)))
    i += 1