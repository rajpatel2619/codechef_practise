n,h,x = input().split()

a=[int(i) for i in input().split()]
done = 0
for i in range(0,int(n)):
    if (a[i]+int(x))>=int(h):
        done=1
        break

print("YES" if done==1 else "NO")
    

