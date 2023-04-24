num = int(input())

channel = []
for i in range(num):
    channel.append(input())

score = 0

k1_num = channel.index('KBS1')   ## 커서 보내기
k2_num = channel.index('KBS2')
if k1_num > k2_num: k2_num += 1
print('1' * k1_num + '4' * k1_num + '1' * k2_num + '4'* (k2_num-1))

### 1234번 다 쓰지 말고 1,4번 만으로 구현하기 이런 생각을 어ㅓ떻게 하지..? ㅠㅠ 
