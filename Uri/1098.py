i = 0.0
j = 0.0

def is_int (x): 
    x *= 10 
    rest = x % 10 
    if rest == 0  or  rest >= 9: 
        return True
    else : 
        return False
    
def show():
    global i 
    global j 

    if is_int(i) :
       for j in range(1, 4):
            j += i 
            print ("I={:.0f} J={:.0f}".format(i, j))
    else : 
        for j in range(1, 4):
                j += i 
                print ("I={:.1f} J={:.1f}".format(i, j))
                
while i <= 2 :
    show() 
    i += 0.2