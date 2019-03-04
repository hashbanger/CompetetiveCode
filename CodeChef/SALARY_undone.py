from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    wages = list(map(int, stdin.readline().strip().split(' ')))
    sum = 0
    maxn = 0
    maxid = 0
    for x in range(len(wages)):
        if wages[x]>=maxn:
            maxid = x
            maxn = wages[x]
    for i in range(len(wages)):
        if i != maxid:
            sum = sum+(maxn - wages[i])

    print(sum)
