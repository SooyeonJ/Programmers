# 두 선수 => 왼 -> 오 | 오 -> 왼 / 중앙 = 물 => 물을 먼저 먹는 선수가 승리
# 칼로리 낮은 음식부터 
# [물(0번), 1번, 2번, 3번, ..]

def solution(food):    
    strings = ''        
    for i, value in enumerate(range(len(food))):
        if i >= 1:            
            strings += str(i) * int((food[i]) // 2)                
    return strings + '0' + ''.join(sorted(strings, reverse=True))