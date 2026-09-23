def solution(s):
    answer = ''                
    return str(min([int(i) for i in s.split()])) + ' ' + str(max([int(i) for i in s.split()]))