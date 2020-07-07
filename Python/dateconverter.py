("""
必要メソッド: 
    _read_time
        引数：無し
        戻り値：float 型の数字
        処理概要：　ユーザーに時間を小数で入力してもらう
""")

def _read_time():

    time = int(input("時間を小数で入力してください:"))
    _validate_time(time)
    _convert_decimal_to_time(time)
    convert_time(time)
("""        　
    _validate_time
        引数：数字
        戻り値：Boolean(True or False)
        処理概要：　指定された数字が0から420の間にあることをチェックする
""")

check=False
def _validate_time(number):
    if 0<number and number<420:
        return True
    print(check)

(""" 
    _convert_decimal_to_time
        引数：数字
        戻り値：変換された時間の文字列　フォーマット：　HH:MM
        処理概要：　指定された数字をHH:MMのフォーマットに変換する
""")

def _convert_decimal_to_time(number):

    if number.find(".") != -1:
        #.から右の数値に掛け算
        hh = left(number.find(".")-1)
        mm = right(len(number)-left(number.find(".")))*60

    else:
        hh = left(number.find(".")-1)
        mm = 0
    return hh & mm
    print(hh&mm)
("""
    covnert_time
        引数：数字
        戻り値：変換された時間の文字列　　フォーマット：　HH:MM
        処理概要：　
            数字が有効範囲外だったらValueErrorを発生させる
            それ以外は指定された数字をHH:MMのフォーマットに変換して変換された文字列を返す
""")

def convert_time(number):
    if [0~9]:
    else:
        print("数値を入力してください")
        _read_time()

("""    
    main
        引数：無し
        戻り値：なし
        処理概要：
            ユーザーの入力を待つ
            入力内容を変換して、表示して処理を終了する
            エラーが発生した場合は、エラーを表示して処理を終了する
""")
#２つ連続すると　）だけ白くなる


#return と　存在[0~9]