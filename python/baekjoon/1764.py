N, M = map(int, input().split())

hear_see = []

hear =  [input().strip() for i in range(N)]
see =  [input().strip() for j in range(M)]

hear_see = list(set(hear)&set(see))

hear_see.sort()
print(len(hear_see))
for x in range(len(hear_see)):
    print(hear_see[x])
