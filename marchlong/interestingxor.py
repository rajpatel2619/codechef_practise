


# import math
# t = int(input())

# for i in range(0,t):
#     c = int(input())
#     d = math.ceil(math.log2(c))
#     tpd = pow(2,d)
#     maxm = 1
#     for a in range(1,tpd):
#         for b in range(2,tpd):
#             if a^b == c:
#                 if a*b > maxm:
#                     maxm = a*b
#     print(maxm)


import math


t = int(input())
for i in range(0,t):
    c = int(input())
    binc =str(bin(c)).split("0b")[1]
    a = "1"
    b = "0"
    for i in range(1,len(binc)):
        if binc[i] == "1":
            a += "0"
            b += "1"
        else:
            a +="1"
            b +="1"
    print(int(a,2)*int(b,2))
    