import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
A_sort = sorted(A, reverse = True)
B_sort = sorted(B)

for i in range(N):
    S += (A_sort[i] * B_sort[i])

print(S)

### 처음엔 B인덱스에 맞춰서 A를 바꾸려고 했는데 이렇게 하면
### 중복된 숫자가 나왔을 때 .index에서 같은 수만 뱉기 때문에 A중에 빈 인덱스가 생김
### 어차피 B를 정렬하든 안하든 S값은 같으므로 위처럼 해결하는게 낫다
