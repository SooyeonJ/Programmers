def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        my_string = my_string.replace(alp, alp.upper())
    answer = my_string
    return answer