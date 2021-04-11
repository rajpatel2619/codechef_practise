t = int(input())

for i in range(0,t):

    group = 0
    s = input()
    
    for j in range(0,len(s)):
        if(j==0 and int(s[j])==1):
            group=group+1
        elif (int(s[j]) == 1 and int(s[j-1])!=1):
            group=group+1
        
    print(group)
        
        
    