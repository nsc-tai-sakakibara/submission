
import random
array =[]

for i in range(0,5,1):
    array.append(random.randrange(1,10,1))


def sort(hairetu):
    print(hairetu)
    suuti=0
    for i in range(0,len(hairetu)-1,1):
    
        suuti+=hairetu[i]

    return suuti

print(array)
ran=sorted(array,reverse=True)
print(sort(ran))

ran=sorted(array)
print(sort(ran))
