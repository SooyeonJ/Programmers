def solution(arr1, arr2):
    answer = []                
    for i, val1 in enumerate(arr1): 
        temp = []
        for j, val2 in enumerate(val1):                                                
            temp.append(val2 + arr2[i][j])
        # print(temp)    
        answer.append(temp)
        
    return answer