from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    dict_terms = {}
    
    for x in terms:
        k1, v1 = x.split(' ')
        dict_terms[k1] = int(v1)
    
    for i, val in enumerate(privacies):
        y, m, d = map(int, val.split(' ')[0].split('.'))
        ty, tm, td = map(int, today.split('.'))
        total_days = y * 12 * 28 + m * 28 + d
        total_todays =  ty * 12 * 28 + tm * 28 + td
        if(total_days + dict_terms[val.split(' ')[1]]*28 <= total_todays):
            answer.append(i+1)
        
        
    return answer
