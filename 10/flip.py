import cv2 as cv
import numpy as np

path = "data/"
img = cv.imread(path + "opencv.png")

print("Original:", img.shape)
cv.imshow("Original", img)
cv.waitKey(0)

# X flip
dst1 = cv.flip(img, 0)
cv.imshow("flipped", dst1)
cv.waitKey(0)

# Y flip
dst2 = cv.flip(img, 1)
cv.imshow("flipped", dst2)
cv.waitKey(0)

dst3 = cv.flip(img, -1)
cv.imshow("flipped", dst3)
cv.waitKey(0)
