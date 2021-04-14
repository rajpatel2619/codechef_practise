t = int(input())
from itertools import groupby
for i in range(0,t):
    n,k = (int(j) for j in input().split())
    string = input()
    flag = 0
    # temp = 0
    res = [(label,len(list(g))) for label, g in groupby(string)]
    for el in res:
        if el[0]=="*":
            if el[1]>=k:
                flag=1
                break
    # for j in range(1,n):
    #     if string[j-1] == string[j] and string[j]=="*":
    #         temp = temp+1
    #         if temp+1==k:
    #             flag=1
    #             break
    #     else:
    #         temp=0
    
        
    
    print("NO" if flag==0 else "YES")

        
    

