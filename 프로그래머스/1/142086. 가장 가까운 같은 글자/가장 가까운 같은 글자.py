def solution(s):
    answer = []
    last_seen = {} # 최근에 본 인덱스 기록
    
    for i, val in enumerate(s):        
        # print(i, val)
        if val in last_seen:            
            distance = i - last_seen[val] # 거리 계산
            answer.append(distance)        
        else: # 처음 본 문자
            answer.append(-1)          
        last_seen[val] = i
    return answer
