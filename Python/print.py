
list =[[0]*10 for i in range(10)]

for i in range(1,11,1):
    for j in range(1,11,1):
        list[i-1][j-1]=i*j
        #print("{} ".format(list[i-1][j-1]),end="")
    
    #print(end="\n")

for i in range(1,11,1):
    for j in range(1,11,1):
        list[i-1][j-1]=str(list[i-1][j-1]).zfill(3)
        print("{} ".format(list[i-1][j-1]),end="")
    
    print(end="\n")

    Time out waiting for launcher to connnect