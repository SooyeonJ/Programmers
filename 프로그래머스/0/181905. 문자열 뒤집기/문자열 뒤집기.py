def solution(my_string, s, e):
    return my_string[:s] + ''.join(list(my_string)[s:e+1][::-1]) + my_string[e+1:]