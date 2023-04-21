n = int(input())
x = [0 for _ in range(n)]
for i in range(n):
    x[i] = (list(map(str, input())))

x_cnt = 0
y_cnt = 0

for i in range(n):
    temp = 0
    y_temp = 0
    for j in range(n):
        if x[i][j] != 'X':
            temp += 1

        elif x[i][j] == 'X':
            if temp >= 2:
                x_cnt += 1
                temp = 0
            else:
                temp = 0

        if x[j][i] != 'X':
            y_temp += 1

        elif x[j][i] == 'X':
            if y_temp >= 2:
                y_cnt += 1
                y_temp = 0
            else:
                y_temp = 0

    if temp >= 2:
        x_cnt += 1
    if y_temp >= 2:
        y_cnt += 1

    temp = 0
    x_flag = False

print(x_cnt, y_cnt)

## 문제 이해를 제대로.. 세로는 i, j 바꾸면 된다! 기억하렴
