def solution(rny_string):
    answer = ''
    for i in rny_string:
        if i == 'm':
            i = i.replace('m','rn')
        answer += i
    return answer