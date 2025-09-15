import cv2 as cv
import numpy as np

path = "data/"
img = cv.imread(path + "opencv.png")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)


h , w, c = img.shape
print("h:", h)
print("w:", w)
print("c:", c)

img2 = np.copy(img)


for row in range(h):
    for col in range(w):
        b , g , r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = b, g, r

cv.imshow("output1", img)
cv.waitKey(0)



for row in range(h):
    for col in range(w):
        b, g, r = img2[row, col]

        # Beyazı siyah yap
        if b == 255 and g == 255 and r == 255:
            img2[row, col] = (0, 0, 0)

        # Siyahı beyaz yap
        elif b == 0 and g == 0 and r == 0:
            img2[row, col] = (255, 255, 255)

cv.imshow("output2", img2)
cv.waitKey(0)