def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        cnt = 0
        r = int(i**0.5) # 루트i
        for d in range(1, r+1):
            if i % d == 0:
                cnt += 2
        if r*r == i:
            cnt -= 1        
        if cnt > limit:
            answer += power 
        else:
            answer += cnt                        
    return answer