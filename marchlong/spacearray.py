t= int(input())
for i in range(0,t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    count = 0
    val = 0 
    for j in range(1,len(a)+1):
        if a[j-1]>j:
            print("Second")
            val=1
            break

    

    if val==0:
        
        for j in range(1,len(a)+1):
            count = count + (j-a[j-1])

        print("Second" if (count%2==0) else "First")