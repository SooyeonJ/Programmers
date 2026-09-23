def solution(s):
    answer = ''
    arr = []
    arr = s.split(' ')
    for i, v1 in enumerate(arr):        
        
        for j, v2 in enumerate(v1):            
            if j % 2 == 0:
                answer += v2.upper()
            else:
                answer +=  v2.lower()
        
        if i < len(arr) - 1:  # 마지막 단어가 아닐 때만 공백 붙이기            
            answer += ' '
    
    return answer