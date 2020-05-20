
def tragetoria (target, v_max):
    x = 0
    hits = 0
    v_now = v_max  

    while v_now > 0: 
        x += v_now 
        hits += 1
        
        if x == target: 
            return("possivel")
        
        elif x > target: 
            s = tragetoria(v_max-1, target) 
            
            if s == "impossivel": 
                break
            else: 
                return("possivel")
            
        elif hits == v_now: 
            s = tragetoria(v_max-1, target) 
            
            if s == "impossivel": 
                break
            else: 
                return("possivel")
                   
    return ("impossivel") 
 

data = input() 
target, v_max = data.split(" ")

while (target != "0") or (v_max != "0"): 
    print(tragetoria(int(target), int(v_max)))
    data = input() 
    target, v_max = data.split(" ")