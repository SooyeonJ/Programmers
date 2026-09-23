def solution(arr, delete_list):
    # answer = []
    # for i in arr:
    #     if i not in delete_list:
    #         answer.append(i)
    
    return [i for i in arr if i not in delete_list]
    # return answer