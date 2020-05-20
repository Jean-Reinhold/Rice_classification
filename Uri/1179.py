def check_individual (media):
    media = int(media)
    if media <= 127: 
        return 0
    else: 
        return 1
    
def is_valid (answer_vec): 
    counter = 0
    
    for answer in answer_vec: 
        if answer == 0: 
            counter += 1
            if counter > 1: 
                return False
    
    if counter == 0: 
        return False
    else: 
        return True 
    
def get_answer (valid_answers): 
    for i in range(len(valid_answers)): 
        if  valid_answers[i] == 0:
            break 
    if i == 0: 
        return "A"
    elif i == 1: 
        return "B" 
    elif i == 2: 
        return "C"
    elif i == 3: 
        return "D"
    elif i == 4: 
        return "E"
    
n = int(input())
while n > 0: 
    i = 0

    while i < n: 
        gross_input = input()
        gross_input = gross_input.split()
    
        answer_vec = [] 
    
        for raw_data in gross_input: 
            answer_vec.append(check_individual(raw_data))
        
        if is_valid(answer_vec): 
            print(get_answer(answer_vec))
        else: 
            print("*") 

        i += 1
        
    n = int(input())
    

    
            
         
        