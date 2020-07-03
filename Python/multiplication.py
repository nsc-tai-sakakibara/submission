
def multiplication(suuti):
    for i in range(0,11,1):
        print("{}×{}={}".format(suuti,i,suuti*i))

number = int(input("数値の入力:"))
multiplication(number)