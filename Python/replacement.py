import random
array=[]

for i in range(0,random.randrange(1,10,1),1):
    array.append(random.randrange(0,50,1))

print(array)

for i in range(1,len(array),1):
    for j in range(1,len(array),1):
        if array[j-1]>array[j]:
            array[j-1],array[j]=array[j],array[j-1]

print(array)