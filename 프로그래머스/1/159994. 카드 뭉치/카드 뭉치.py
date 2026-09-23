def solution(cards1, cards2, goal):
    answer = 'Yes'
    for val in goal:                
        if cards1 and cards1[0] == val:
            cards1.pop(0)
        elif cards2 and cards2[0] == val:
            cards2.pop(0)
        else:
            answer = 'No'
        
    return answer