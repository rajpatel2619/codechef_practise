t = int(input())
for i in range(0,t):
    k1,k2,k3,v = (float(j) for j in input().split())
    print("YES" if(round(100/(k1*k2*k3*v) , 2) < 9.58) else "NO")