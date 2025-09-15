import cv2 as cv
import numpy as np

# Video kaynağı
capture = cv.VideoCapture("data/video.mov")

# Video özellikleri
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
fps = capture.get(cv.CAP_PROP_FPS)

print("height:", height, ", width:", width, ", count:", count, ", fps:", fps)

# VideoWriter nesnesi
fourcc = cv.VideoWriter_fourcc(*"DIVX")  # "XVID" veya "MJPG" da kullanılabilir
out = cv.VideoWriter("data/video.avi", fourcc, 30, (width, height), True)

# Video okuma ve yazma örneği
while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow("frame", frame)
        out.write(frame)
        c = cv.waitKey(50)
        if c == 27:
            break
    else:
        break

capture.release()
out.release()