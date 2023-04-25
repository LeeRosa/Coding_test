country_num, check_num = map(int, input().split())

medal = [0] * country_num
for i in range(country_num):
    num = list(map(int,input().split()))
    medal[num[0]-1] = num[1:]

check_country = medal[check_num-1]

medal.sort(reverse=True)

print(medal.index(check_country)+1)

### 문제 잘 읽자!! 그래도 한 방에 100점!
