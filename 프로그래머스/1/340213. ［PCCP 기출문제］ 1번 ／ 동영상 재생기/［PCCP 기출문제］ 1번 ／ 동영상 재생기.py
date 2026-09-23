def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    sec_pos = 0
    sec_op_start = 0
    sec_op_end = 0  
    sec_video = 0
    
    # 10초 전 이동 - prev / 10초 후 이동 - next / 건너뛰기 - 현재 재생위치...
        
    sec_pos = int(pos[:2]) * 60 + int(pos[3:])
    sec_op_start = int(op_start[:2]) * 60 + int(op_start[3:])
    sec_op_end = int(op_end[:2]) * 60 + int(op_end[3:])
    sec_video = int(video_len[:2]) * 60 + int(video_len[3:])

    if (sec_pos >= sec_op_start) and (sec_pos < sec_op_end):
        sec_pos = sec_op_end    
        
    for i in commands:                            
        if i == 'prev': sec_pos = sec_pos - 10
        elif i == 'next': sec_pos = sec_pos + 10                                   
            
        if sec_pos < 0: sec_pos = 0                                        
        if sec_pos > sec_video: sec_pos = sec_video
        
        if (sec_pos >= sec_op_start) and (sec_pos < sec_op_end):
            sec_pos = sec_op_end
            
    return str(sec_pos // 60).zfill(2) + ':' + str(sec_pos % 60).zfill(2)