
suuti = int(input("数値を入力してください："))


if suuti %2 == 1:
    print("奇数です")
else:
    print("偶数です")

def divide(array):
    evenNumber=[]
    oddNumber=[]
    for i in range(0,len(array),1):
        if array[i]%2==0:
            evenNumber.append(array[i])
        else:
            oddNumber.append(array[i])
    print("偶数：",evenNumber)
    print("奇数：",oddNumber)

array=[1,2,3,4,5,6]
print("元のarray:",array)

divide(array)