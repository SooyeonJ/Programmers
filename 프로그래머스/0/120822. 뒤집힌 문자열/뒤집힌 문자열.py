def solution(my_string):
    answer = ''
    for i in list(my_string[::-1]):
        answer += i
    return answer