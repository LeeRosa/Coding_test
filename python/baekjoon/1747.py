import math
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False        
    return True

def is_palin(num_str):
    for i in range(int(len(num_str)/2)+1):
        if num_str[i] is not num_str[len(num_str)-1-i]:
            return False
    return True

num = int(input())
while(1):
    if is_prime(num) == True:
        if is_palin(str(num)) == True:
            print(num)
            break
    num += 1

## 이중 if문으로 할게 아니라
### if is_prime(num) and is_palin(str(num)):
### 으로 했어도 됐음 
