def solution(name, yearning, photo):
    answer = []
    aa = 0
    my_dict = []
    my_dict = dict(zip(name, yearning))
    for i in photo:    
        aa = 0 # 반드시 초기화!       
        for j in i:
            aa += my_dict.get(j, 0)                
        answer.append(aa)
    return answer