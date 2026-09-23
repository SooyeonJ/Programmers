def solution(t, p):    
    arr = []
    # 012 123 234 345 456 567 (7-3+1)
    # 부분문자열 개수 => len(t) - len(p) + 1
    for i in range(len(t)):
        if len(t[i:i+len(p)]) == len(p):
            if t[i:i+len(p)] <= p:                    
                arr.append(t[i:i+len(p)])
    return len(arr)