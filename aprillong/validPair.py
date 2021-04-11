a,b,c = (int(i) for i in input().split())
print("YES" if(a==b or b==c or c==a) else "NO")
