import random
array=[]
arrayAverage=0

for i in range(0,random.randrange(5,10,1),1):
    array.append(random.randrange(0,50,1))

for i in range(0,len(array),1):
    arrayAverage += array[i]

a = arrayAverage // len(array)
arrayAverage %= len(array)
print(array)
print("平均",a,end="")
print("余り{}".format(arrayAverage))