
length = int(input("縦の長さを入力してください："))
width = int(input("横の長さを入力してください："))

def range(suuti):
    while (suuti<1) or (1000<suuti):
        print("有効範囲は　1～1000　です。")
        print("値を入れなおしてください。")
        suuti = int(input(":"))
    return int(suuti)

if (length<1)or(1000<length):
    print("縦の長さが有効範囲外です")
    length=range(length)
    
if (width<1)or(1000<width):
    print("横の長さが有効範囲外です")
    width=range(width)
    
print("面積は"+str(length*width))