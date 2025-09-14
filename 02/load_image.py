import cv2 as cv
import numpy as np
# ---- 1. Görselin yolu ----
path = "data/"


img1 = cv.imread(path + "test_image1.png")
img2 = cv.imread(path + "test_image2.png")


h , w , ch = img1.shape

print("h:" , h)
print("w:" , w)
print("ch:" , ch)

# add
add_result = np.zeros(img1.shape,img1.dtype)
cv.add(img1,img2,add_result)
cv.imshow("add_result",add_result)
cv.waitKey(0)

# substract
subtract_result = np.zeros(img1.shape,img1.dtype)
cv.subtract(img1,img2,subtract_result)
cv.imshow("subtract_result",subtract_result)
cv.waitKey(0)

# multiply
multiply_result = np.zeros(img1.shape,img1.dtype)
cv.multiply(img1,img2,multiply_result)
cv.imshow("multiply_result",multiply_result)
cv.waitKey(0)

# division
divide_result = np.zeros(img1.shape,img1.dtype)
cv.divide(img1,img2,divide_result)
cv.imshow("divide_result",divide_result)
cv.waitKey(0)

cv.destroyAllWindows()