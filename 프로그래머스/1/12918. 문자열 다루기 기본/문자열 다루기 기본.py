def solution(s):    
    answer = False
    if (s.isdigit() == True):
        if ((len(s) == 4) or (len(s) == 6)):
            answer = True
    else: 
        answer = False
    return answer