it = int(input())

# def checkPossible(n,e,h):
#     t=n
#     for i in range(0,n):
#         if e < 1 and h<1 and t>0:
#             return False

#         if (e > 0 and h > 0):
#             if t>0:
#                 e=e-1
#                 h=h-1
#                 t=t-1
#             else:
#                 return True
            
#             continue
        
#         if (e < 1 and h > 2):
#             if t>0:
#                 h=h-3
#                 t=t-1
#             else:
#                 return True
            
#             continue
    
#         if (e > 1 and h < 1):
#             if t>0:
#                 e=e-2
#                 t=t-1
#             else:
#                 return True
            
#             continue

#         if(e==0 and h<3 and t>0):
#             return False
        
#         if(h==0 and e<2 and t>0):
#             return False


#     return True
        

                




for i in range(0,it):
    n,e,h,a,b,c = (int(j) for j in input().split())
    # friends,eggs,choco bars, op,cmp,ccp
   
    # possible =  checkPossible(n,e,h)

    # if not possible:
    #     res = -1
    #     print(res)
    #     continue

    # print("next part")
    price = 0
    tmp = n 
    arr =[a,b,c]
    for k in range(0,3):
        if n>0:
            min1 = min(arr)
            arr.remove(min1)
            
            if min1==a:
                while(e>1 and n>0):
                    e=e-2
                    n=n-1
                    price = price + a
            elif min1 == b:
                while(h>2 and n>0):
                    h=h-3
                    n=n-1
                    price = price+b
            else:
                while(e>0 and h>0 and n>0):
                    e=e-1
                    h=h-1
                    n=n-1
                    price=price+c
        
    print(price if n < 1 else "-1")

            
