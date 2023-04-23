color = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
num = {1: 0, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
temp_num = []
arr = []
[arr.append(input().split()) for i in range(5)]

score = 0

for i in range(5):
    num[int(arr[i][1])] += 1
    for color_ in color:
        color[color_] += arr[i].count(color_)

for k, v in num.items():
    if v > 0:
        temp_num.append(k)

max_color = max(color.values())
max_num = max(num.values())
max_temp_num = max(temp_num)

if max_color == 5:
    if max_num == 1 and max_temp_num - min(temp_num) == 4:
        score = int(max_temp_num) + 900
    else:
        score = max(temp_num) + 600

elif max_num == 4:
    score = max(num, key=num.get) + 800

elif max_num == 3:
    second_num = [k for k, v in num.items() if v == 2]
    if second_num:
        score = max(num, key=num.get) * 10 + second_num[0] + 700
    else:
        score = max(num, key=num.get) + 400

elif max_num == 2:
    second_num = [k for k, v in num.items() if v == 2]
    if len(second_num) == 2:
        score = max(second_num) * 10 + min(second_num) + 300

    else:
        score =  200 + max(num, key=num.get)

elif max_num == 1 and max_temp_num - min(temp_num) == 4:
    score = max_temp_num + 500

else:
    score = max_temp_num + 100

print(score)

### score = 이런거 빼먹어서 이상하게 틀리는 실수.. 고쳐라...ㅠ
