import cv2 as cv
import numpy as np

path = "data/"
img = cv.imread(path + "tech_pp.png")   # Görseli oku

# cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
# cv.imshow("image",img)
# cv.waitKey(0)

m1 = np.copy(img)
m2 = img
print(type(m1)) # -> numpy array


img[200:350,250:700 ,:] = 255
# cv.imshow("image",img)
# cv.waitKey(0)

img = np.ones((550,770,3))
black = (0,0,0)
red = (0,0,255)
green = (0,255,0)

# Dikdörtgen boyutu
top_left = (150, 250)
bottom_right = (480, 450)

# İlk dikdörtgen
cv.rectangle(img, top_left, bottom_right, black, 8)

# Ofset belirle (x, y)
dx, dy = 100, -100

# İkinci dikdörtgen (aynı boyutta, yukarı kaydırılmış)
top_left2 = (top_left[0] + dx, top_left[1] + dy)
bottom_right2 = (bottom_right[0] + dx, bottom_right[1] + dy)
cv.rectangle(img, top_left2, bottom_right2, black, 8)

# Köşeleri bağla
cv.line(img, top_left, top_left2, black, 8)               # sol üst
cv.line(img, (bottom_right[0], top_left[1]), (bottom_right2[0], top_left2[1]), black, 8)  # sağ üst
cv.line(img, (top_left[0], bottom_right[1]), (top_left2[0], bottom_right2[1]), black, 8)  # sol alt
cv.line(img, bottom_right, bottom_right2, black, 8)       # sağ alt


start_point = (150,100)
font_thickness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX

cv.putText(img,"Muhammed Aydin",start_point,font,font_size,black,font_thickness)
cv.imshow("Dikdörtgen",img)
cv.waitKey(0)

cv.destroyAllWindows()