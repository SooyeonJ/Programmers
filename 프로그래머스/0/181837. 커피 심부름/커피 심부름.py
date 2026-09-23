def solution(order):
    answer = 0
    # 아메 4500, 라떼 5000
    for i in order:
        if 'cafelatte' in i:            
            answer += 5000
        elif 'americano' or 'anything' in i:            
            answer += 4500
    return answer