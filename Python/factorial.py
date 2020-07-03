
suuti=int(input("値を入力してください:"))
list=[]

def factorial(suuti):
    solution=1
    while suuti>1:

        solution*=suuti
        list.append(suuti)
        suuti-=1
    print("{} =".format(solution), end="")

factorial(suuti)

for i in range(0,len(list),1):
    print(" *",list[i],end="")

# *の数を調整　ループもう一つ作ってしまう