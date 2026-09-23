def solution(n):
    answer = 0
    arr = []
    for i in list(str(n)):
        arr.append(int(i))
    arr = sorted(arr, reverse=True)
    print(int(''.join(arr)))
    # print(''.join(str(sorted(arr, reverse=True)))
    return answer