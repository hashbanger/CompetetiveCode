# https://www.codechef.com/MARCH15/problems/CNOTE

from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    X, Y, K, N = map(int, stdin.readline().strip().split(' '))
    flag = 0
    for i in range(N):
        Pi, Ci = map(int, stdin.readline().strip().split(' '))
        if Ci<= K and Pi>= X-Y:
                flag = 1
                
    if flag == 1:
        print('LuckyChef')
    else:
        print('UnluckyChef')