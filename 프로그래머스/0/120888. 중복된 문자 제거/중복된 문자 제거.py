from collections import Counter

def solution(my_string):
    answer = ''    
    for i in Counter(my_string):
        print(i)
        answer += i        
    return answer