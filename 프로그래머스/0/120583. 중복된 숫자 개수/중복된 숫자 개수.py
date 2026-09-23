def solution(array, n):
    answer = 0
    for i in array:
        if n == i:
            return array.count(i)
    return answer