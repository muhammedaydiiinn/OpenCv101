import cv2 as cv
import numpy as np

path = "data/"
img = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE)

# minMaxLoc

min_value , max_value ,min_loc , max_loc = cv.minMaxLoc(img)
print(min_value,"->", min_loc)
print(max_value,"->", max_loc)

means, std_dev = cv.meanStdDev(img)

mean_val = means[0, 0]     # (1x1 array → tek eleman)
std_val  = std_dev[0, 0]

print(f"mean: {mean_val:.2f}, std_dev: {std_val:.2f}")

img[np.where(img < mean_val)] = 0
img[np.where(img >= mean_val)] = 255
cv.imshow("img", img)
cv.waitKey(0)