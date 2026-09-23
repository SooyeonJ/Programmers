def solution(n):
    answer = 0    
    for i in range((n//2)+1):  
        if (n % 2) != 0: # n = 7, i = 0 ~ 3            
            answer += (2*i) + 1 # 1, 3, 5, 7            
        else: # n = 10, i = 0 ~ 5
            answer += (2*i)*(2*i) # 0, 4, 16, .. 100            
    return answer