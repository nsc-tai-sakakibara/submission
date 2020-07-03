
suuti = int(input("値入力:"))
def sosuu(suuti):
    for i in range(2,suuti,1):
        if suuti%i==0:
            print("{}は素数ではない".format(suuti))
            #return False
            break
        
if suuti<=0:
    print("{}は素数ではない".format(suuti))
elif suuti==1:
    print("{}は素数である".format(suuti))
else:
    if sosuu(suuti)==True:
        print("{}は素数である".format(suuti))
