def cycle(num):
    if num < 0:
        result_num = (num * 10) + num
    else:
        result_num = ((num % 10) * 10) + (((num // 10) + (num % 10)) % 10)

    return result_num


initial_num = int(input())
cnt = 0
num = initial_num

while(True):
    cnt += 1
    num = cycle(num)
    if initial_num == num:
        print(cnt)
        break
