
list=[]

times = int(input("値の入力:"))
i=2
        
list.append(0)
list.append(1)


print(list)
while i <= times:
    
    list.append(list[i-2]+list[i-1])

    i+=1
print(list)