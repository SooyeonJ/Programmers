def solution(myString):
    answer = []    
    arr = []
    arr = myString.split('x')
    for i in range(len(arr)):
        answer.append(len(arr[i]))
    return answer