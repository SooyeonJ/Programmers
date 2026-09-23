def solution(numbers):
    return sorted(numbers)[::-1][0] * sorted(numbers)[::-1][1]