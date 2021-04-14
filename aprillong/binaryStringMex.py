t  = int(input())
for i in range(t):
    string = input()


    flag=0
    length = len(string)
    index = 0


    num = int(string,2)

    # def check(string,cha,ind,length):
    #     for it in range(ind+1,length):
    #         if string[it]==cha:
    #             return it
    #         else:
    #             return -1
    
    for j in range(num):
        if flag != 1:
            binaryString = str(bin(num)[2:])
            for k in range(len(binaryString)):
                # nindex = check(string,binaryString[k],index,length);
                for it in range(index+1,length):
                    if string[it]==binaryString[k]:
                        index = it
                    else:
                        index =-1

                if index==-1:
                    flag=1
                    print(bin(j)[2:])
                    break





