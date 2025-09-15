import cv2 as cv
import numpy as np

# Video kaynağı
capture = cv.VideoCapture(0)  # CAP_ANY macOS’da mevcut en uygun kamerayı seçer

height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
height = int(height)
width = int(width)

print("fps:", fps, "count:", count, "width:", width, "height:", height)

def process(image,opt=1):
    dst= None
    if opt == 0:
        dst = cv.bitwise_not(image)
    if opt == 1:
        dst = cv.GaussianBlur(image,(0,0),15)
    if opt == 2:
        dst = cv.Canny(image,100,200)
    return dst

index = 0
while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow("frame", frame)
        c = cv.waitKey(50)
        if c >= 49:
            index = c -49
        result = process(frame,index)
        cv.imshow("result", result)

        if c == 27:
            break
    else:
        break



