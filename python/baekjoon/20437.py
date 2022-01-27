import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
W = ['']*T
K = [0]*T

for a in range(T):
    W[a] = input()
    K[a] = int(input())

def game(w, k):
    if k == 1:
        return 1, 1
    else:
        length = len(w)
        minimum = length
        maximum = 0
        string_input = defaultdict(list)

        for j in range(length):
            if w.count(w[j]) >= k:
                string_input[w[j]].append(j)

        if not string_input:
            return -1,

        for z in string_input.values():
            for y in range(len(z)-k+1):
                abs_jz = z[y+k-1]-z[y]+1
                if maximum < abs_jz:
                    maximum = abs_jz
                if minimum > abs_jz:
                    minimum = abs_jz

        return minimum, maximum

for i in range(T):
    print(*game(W[i], K[i]))
