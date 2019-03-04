from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    flag = 0
    c1 = 1
    c2 = 7
    arr_length = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    if (max(arr)==7) and (min(arr)==1):
        mid = int(arr_length/2)
        if(int(arr_length % 2) ==0):
            a1 = arr[:mid]
            a2 = arr[mid:]
        else:
            a1 =  arr[:mid]
            a2 = arr[mid+1:]
        r = a1[len(a1)-1]
        for i in range(0, len(a1)):
            if (a1[len(a1)-i-1] == r or a1[len(a1)-i-1] == r-1  ) and (a2[i] ==r or a2[i] == r-1) :
                if a1[len(a1)-i-1] == a2[i]:
                    r=a2[i]
                else:
                    flag = 1
            else:
                flag = 1
    else:
        flag = 1
        
if flag ==1:
    print('no')
elif flag==0 and mid == 7 :
    print('yes')

print("a1:",a1)
print("a2:",a2)
        # for n in arr:
        #     if(n==c1) or (n==c1+1):
        #         c1 = n
        #     elif (n==c2) or (n==c2-1):
        #         c2 = n
        #     else:
        #         flag = 1
        #         break
            
