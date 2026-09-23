def solution(a, b):
    days = ['SUN', 'MON' ,'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month_days = [31,29,31,30,31,30,31,31,30,31,30,31] # 윤년(2월:29일)
    
    # print(month_days[0:a-1] + (b - 1)) # 이전 달들 날짜 합
    a = (sum(month_days[0:a-1]) + (b-1)) % 7
    return days[a-2]