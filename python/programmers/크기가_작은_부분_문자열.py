import math
def solution(t, p):
    new_cut = []
    start = 0
    end = 0
    
    while(end < len(t)):
        end = start+len(p)
        new_cut.append(t[start:end])
        start += 1
        
    ### 이 while문 
    '''
    for i in range(len(t)-len(p)+1):
      new_cut.append(t[i:i+len(p)]
      
     다음부터 불필요한 변수 쓰지 말고 이렇게 짜자ㅠ
    '''
        
    cnt = 0
    for j in new_cut:
        if int(j) <= int(p):
            cnt += 1

    answer = cnt
    ### 이것도 count 쓰지 말고 answer 정수로 사용했으면 될 일 ! 
    return answer
  
  
  
