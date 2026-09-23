def solution(s):
    answer = True
    p = len([i for i in list(s) if i == 'P' or i == 'p'])
    y = len([i for i in list(s) if i == 'Y' or i == 'y'])
    if p != y:
        answer = False
    return answer