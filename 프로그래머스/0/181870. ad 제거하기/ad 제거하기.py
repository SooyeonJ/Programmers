def solution(strArr):
    delete_list = []
    for i in strArr:
        if 'ad' in i:
            delete_list.append(i)
    strArr = [x for x in strArr if x not in delete_list]
    return strArr