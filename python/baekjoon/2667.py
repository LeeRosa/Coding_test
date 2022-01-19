dange_size = input()
dange = []
for i in range(int(dange_size)):
    input_data = input()
    dange.append(input_data)
flag = [[0]*int(dange_size) for _ in range(int(dange_size))]

num = 1
num_home_list = []
num_home = 1

def dfs(dange, j, k, flag, num_home):
    if k+1 != len(dange[0]) and dange[j][k + 1] == '1' and flag[j][k+1] == 0:  # 오른쪽이랑 비교
        flag[j][k+1] = 1
        num_home = dfs(dange, j, k+1, flag, num_home) + 1
    if k-1 != -1 and dange[j][k - 1] == '1' and flag[j][k-1] == 0: # 왼쪽이랑 비교
        flag[j][k-1] = 1
        num_home = dfs(dange, j, k-1, flag, num_home) + 1
    if j+1 != len(dange[0]) and dange[j + 1][k] == '1' and flag[j + 1][k] == 0: # 아래쪽이랑 비교
        flag[j + 1][k] = 1
        num_home = dfs(dange, j+1, k, flag, num_home) + 1
    if j-1 != -1 and dange[j - 1][k] == '1' and flag[j - 1][k] == 0: # 위쪽이랑 비교
        flag[j - 1][k] = 1
        num_home = dfs(dange, j - 1, k, flag, num_home) + 1
    return num_home

for x in range(int(dange_size)):
    for y in range(int(dange_size)):
        if dange[x][y] == '1' and flag[x][y] == 0:
            num_home = 1
            flag[x][y] = 1
            num_home = dfs(dange, x, y, flag, num_home)
            num_home_list.append(num_home)

num_home_list.sort()
print(len(num_home_list))
for a in range(len(num_home_list)):
    print(num_home_list[a])
