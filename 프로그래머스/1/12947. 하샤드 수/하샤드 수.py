def solution(x):
    answer = True            
    if int(x % sum([int(i) for i in str(x)])) != 0: # 히샤드 수        
        answer = False
    return answer