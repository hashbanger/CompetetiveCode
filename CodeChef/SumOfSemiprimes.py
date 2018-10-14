from sys import stdin
import math 

def prime(x):
    if x != 1:
        result = True
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                result = False
                break
        return result            
    else:
        return False 

def checkSemiprime(num): 
    for i in range(2, num):
        if num % i == 0:
            if prime(i) == True:
                p1 = i
                p2 = int(num/i)
                if prime(p2) == True and (p1 != p2):
                    return True
    
    return False
    

def semiprime(n): 
    if checkSemiprime(n) == True: 
        return True 
    else: 
        return False 
  

#print("Enter number")
tcase = int(stdin.readline()) 
for t in range(tcase):
    fnum = int(stdin.readline())

    sp_dic = {}
    result = "NO"
    for i in range(4, fnum):
        if i not in sp_dic:
            if semiprime(i) == True:
                sp_dic[i] = "Y"
                if semiprime((fnum - i)) == True:
                    #print("reached for",i)
                    result = "YES"
                    break 
                else:
                    sp_dic[(fnum - i)] = "N"
    # print(semiprime(27))
    # print(sp_dic)
    print(result)

