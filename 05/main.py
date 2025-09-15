import cv2 as cv
import numpy as np

path = "data/"
img = cv.imread(path + "opencv.png")

# spilt the channels
mv = cv.split(img)

print(mv)

mv[0][:, :] = 0

dst1 = cv.merge(mv)
cv.imshow("dst1", dst1)
cv.waitKey(0)

mv = cv.split(img)

mv[1][:, :] = 0

dst2 = cv.merge(mv)
cv.imshow("dst2", dst2)
cv.waitKey(0)