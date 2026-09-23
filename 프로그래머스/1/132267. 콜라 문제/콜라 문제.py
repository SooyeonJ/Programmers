def solution(a, b, n):
    # n = n - a + b
    answer = 0
    while (n >= a):
        answer += b
        n = n - a + b
        
    return answer