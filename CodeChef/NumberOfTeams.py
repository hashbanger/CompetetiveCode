from sys import stdin
tcase = int(stdin.readline())
for _ in range(0,tcase):
    n, k = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    set_arr = sorted(arr,reverse = True)
    minScore = set_arr[k-1]   
    count = 0 
    for team in arr:
        if team >= minScore:
            count = count +1
    print(count)







