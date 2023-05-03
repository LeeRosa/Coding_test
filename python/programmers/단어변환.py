from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(begin, target, words, visited, cnt_list, cnt):
    queue = deque()
    visited.append(begin)
    
    for word in words:
        temp_cnt = 0
        for i in range(len(begin)):
            if begin[i] == word[i]:
                temp_cnt += 1
        if temp_cnt >= len(begin)-1:
            if word not in visited:
                queue.append(word)
            
    while queue:
        v = queue.popleft()
        if v == target:
            cnt += 1
            cnt_list.append(cnt)
        else:
            cnt += 1
            dfs(v, target, words, visited, cnt_list, cnt)
            cnt -= 1

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    visited = []
    cnt = 0
    cnt_list = []
    dfs(begin, target, words, visited, cnt_list, cnt)
    if len(cnt_list) > 0:
        answer = min(cnt_list)
    else:
        answer = 0
    return answer
  
  
  ######## 문자의 길이가 3이상인 것 주의 (2개 이상 같은 조건으로 했따가 계속 틀림)
  ######## queue 에서 빼고 나서 다음 큐에서 뺄 때 cnt 를 하나 빼줘야함
  ######## 처음에 set으로 바꿔서 교집합 찾는거로 했었는데 이렇게 하니까 hhh와 hht의 교집합이 h 하나로 인식 --> 그냥 포문 돌림
