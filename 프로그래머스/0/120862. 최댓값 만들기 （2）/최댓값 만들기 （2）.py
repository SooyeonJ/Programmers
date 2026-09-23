def solution(numbers):
    arr = []
    arr = sorted(list(numbers))    
    for i in arr:
        if (arr[0] * arr[1]) >= (arr[len(arr)-2] * arr[len(arr)-1]):
            return arr[0] * arr[1]
        else: 
            return arr[len(arr)-2] * arr[len(arr)-1]