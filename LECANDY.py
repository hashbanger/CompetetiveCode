from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n, c = map(int, stdin.readline().strip().split(' '))
    ele = list(map(int, stdin.readline().strip().split(' ')))
    if (sum(ele) <= c):
        print("Yes")
    else:
        print("No")