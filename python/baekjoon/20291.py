import sys
input = sys.stdin.readline

N = int(input())
ext = {}
for i in range(N):
    f_n = input().strip()
    file_name = f_n.split('.')[1]
    if file_name not in ext:
        ext[file_name] = 1
    else:
        ext[file_name] += 1

file_name = list(ext.keys())

file_name.sort()
for z in file_name:
    print(z, ext[z])
