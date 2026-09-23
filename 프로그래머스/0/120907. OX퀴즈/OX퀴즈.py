def solution(quiz):
    answer = []
    arr = []    
        
    arr = [i.split(' ') for i in quiz]    
    
    for k, v in enumerate(arr):
        if (v[1] == '+') and (int(v[0]) + int(v[2]) == int(v[4])):
            answer.append("O")            
        elif (v[1] == '-') and (int(v[0]) - int(v[2]) == int(v[4])): 
            answer.append("O")            
        else:
            answer.append("X")            
    
    return answer