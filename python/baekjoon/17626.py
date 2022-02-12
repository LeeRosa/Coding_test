import sys
import math
input = sys.stdin.readline

num = int(input())

def dp(num):
    if int(math.sqrt(num)) == math.sqrt(num):
        return 1
    for i in range(1, int(math.sqrt(num))+1):
        if int(math.sqrt(num-math.pow(i, 2))) == math.sqrt(num-math.pow(i, 2)):
            return 2
    for i in range(1, int(math.sqrt(num))+1):
        for j in range(1, int(math.sqrt(num-math.pow(i, 2)))+1):
            if int(math.sqrt(num-math.pow(i, 2)-math.pow(j, 2))) == math.sqrt(num-math.pow(i, 2)-math.pow(j, 2)):
                return 3
    return 4

print(dp(num))
