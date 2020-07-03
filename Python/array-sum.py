
import random
array=[]
arraySum=0

random.seed()

for i in range(0,random.randrange(5,10,1),1):
    array.append(random.randrange(0,50,1))

for i in range(0,len(array),1):
    arraySum+=array[i]

print(array)
print(arraySum)