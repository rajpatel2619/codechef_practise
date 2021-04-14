term = int(input())
for i in range(term):
    n = int(input())
    if n==1:
        print(20)
    elif n==2:
        print(36)
    elif n==3:
        print(51)
    elif n==4:
        print(60)
    
    else:
        reminder = n%4
        answer = ((n-reminder)//4)*44

        if reminder==0:
            answer=answer+16
        elif reminder==1:
            answer=answer+ 32
        elif reminder==2:
            answer=answer+44
        elif reminder==3:
            answer=answer+55
        

        print(answer)



