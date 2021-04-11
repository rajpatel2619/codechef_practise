t = int(input())
for i in range(0,t):
    n,k = (int(j) for j in input().split())
    string = input()
    flag = 0
    temp = 0
    for j in range(1,n):
        if string[j-1] == string[j] and string[j]=="*":
            temp = temp+1
            if temp+1==k:
                flag=1
                break
        else:
            temp=0
        
    
    print("NO" if flag==0 else "YES")

        
    

