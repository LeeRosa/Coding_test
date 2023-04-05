def solution(name, yearning, photo):
    
    answer = []
    for j in range(len(photo)):
        score = 0
        for i in range(len(name)):
            if name[i] in photo[j]:
                score += yearning[i]
        answer.append(score)

    return answer
  
  ### 너무 무지서 느낌. python의 문법을 이용해서 간단하게 짤 필요가 있어보임 
