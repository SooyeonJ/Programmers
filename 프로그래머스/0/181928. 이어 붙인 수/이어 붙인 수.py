def solution(num_list):
    stra = ''
    strb = ''
    for i in num_list:
        if i % 2 == 0:
            stra += str(i)
        else:
            strb += str(i)
    return int(stra)+int(strb)