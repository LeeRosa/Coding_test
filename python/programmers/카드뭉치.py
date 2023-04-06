def solution(cards1, cards2, goal):
    answer = ''
    index1 = 0
    index2 = 0
    for word in goal:          
        if index1 < len(cards1) and word == cards1[index1]:
            index1 += 1
            
        elif index2 < len(cards2) and word == cards2[index2]:
            index2 += 1
            
        else:
            answer = "No"            
            return answer
            
    answer = "Yes"
    return answer
  
  ##### 다음에 pop() 을 써서 불필요한 변수를 쓰지 말자
