def solution(numbers, n):
    s1 = 0
    for i in numbers:
        s1 += i
        if s1 > n:
            return s1