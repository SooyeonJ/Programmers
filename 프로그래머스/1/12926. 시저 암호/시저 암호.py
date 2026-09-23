def solution(s, n):
    answer = ''
    # print([chr(ord(i)+n) for i in list(s)])
    print([ord(i) for i in list(s) if i != ' '], [i for i in list(s) if i != ' '])
    
    # print([ord(i)+n for i in list(s) if i != ' '])
    for i in [ord(i) for i in list(s) if i != ' ']:
        print((i - ord('a')) % 26)
        
    return answer