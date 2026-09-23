def solution(myString, pat):        
    myString2 = ''
    for i in myString:
        if i == 'A':        
            i = i.replace('A', 'B')            
        else:
            i = i.replace('B', 'A')
        myString2 += i
    if pat in myString2: return 1
    else: return 0
    