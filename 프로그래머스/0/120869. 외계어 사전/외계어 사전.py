from itertools import permutations
def solution(spell, dic):
    answer = 0
    result = [''.join(p) for p in permutations(spell, len(spell))]
    if len(set(result) & set(dic)) >= 1:
        return 1
    else: 
        return 2
    return answer