def solution(s):
    answer = ''
    sarr = []
    sarr = s.split(' ')
    
    for i, val in enumerate(sarr):        
        if val == '':
            answer += ' '          # ✅ 빈 토큰은 공백만 추가하고 건너뜀
            continue
        if not val[0].isdigit():                        
            sarr[i] = val[0].upper() + val[1:].lower()                    
        else:
            sarr[i] = val.lower()
        answer += sarr[i] + ' '   
    print(sarr, answer)    
    return answer[:-1]