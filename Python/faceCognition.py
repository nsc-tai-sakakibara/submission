import cv2
from PIL import Image,ImageFont,ImageDraw
import numpy as np

#putText の代わりの日本語表示関数
def imgMsg(img, message):
    font_path = 'C:\Windows\Fonts\meiryo.ttc'
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), message, font=font, fill=(0, 0, 255, 0))
    img = np.array(img)
    return img

#opencv 顔と目の認識用ファイル
faceCascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
eyeCascadePath = cv2.data.haarcascades + 'haarcascade_eye.xml'

faceCascade = cv2.CascadeClassifier(faceCascadePath)
eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

#デフォルト
cam = cv2.VideoCapture(0)

#メッセージ内容
message='Esc キーで終了します'

while True:
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.41, minNeighbors=5)

    #認識範囲調整
    for x, y, w, h in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face = img[y: y + h, x: x + w]

        faceGray = gray[y: y + h, x: x + w]
        eyes = eyeCascade.detectMultiScale(faceGray, scaleFactor=1.61, minNeighbors=5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    #映像出力
    img = imgMsg(img, message)
    cv2.imshow('video image', img)
    
    #10msec　入力待ち
    key = cv2.waitKey(10)
    # ESCキーで終了
    if key == 27:
        break

#キャプチャ終了
cam.release()
cv2.destroyAllWindows()