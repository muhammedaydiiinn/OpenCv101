import cv2 as cv
import numpy as np

path = "data/"
img = cv.imread(path + "opencv.png")

print("Original:", img.shape)

# ---- 1. Griye çevir ----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(0)

print("Gray shape:", gray.shape)

# float32'e çevir
gray = np.float32(gray)

# ---- 2. Min–Max Normalizasyonu (0–1 arası) ----
dst_minmax = np.zeros_like(gray)
cv.normalize(gray, dst=dst_minmax, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
cv.imshow("Min-Max [0-1]", dst_minmax)
cv.waitKey(0)

# ---- 3. Min–Max Normalizasyonu (0–255 arası) ----
dst_minmax_255 = np.zeros_like(gray)
cv.normalize(gray, dst=dst_minmax_255, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
dst_minmax_255 = np.uint8(dst_minmax_255)
cv.imshow("Min-Max [0-255]", dst_minmax_255)
cv.waitKey(0)

# ---- 4. L2 Normalizasyonu (Vektör uzunluğunu 1 yapar) ----
dst_l2 = np.zeros_like(gray)
cv.normalize(gray, dst=dst_l2, alpha=1.0, beta=0.0, norm_type=cv.NORM_L2)
cv.imshow("L2 Normalized", dst_l2)
cv.waitKey(0)

# ---- 5. Z-Score Normalizasyonu (Ortalama=0, Std=1) ----
mean, stddev = cv.meanStdDev(gray)
zscore = (gray - mean[0][0]) / (stddev[0][0] + 1e-8)
# Görüntülemek için 0-255 aralığına yeniden ölçekleyelim
zscore_vis = cv.normalize(zscore, None, 0, 255, cv.NORM_MINMAX)
zscore_vis = np.uint8(zscore_vis)
cv.imshow("Z-Score Normalized", zscore_vis)
cv.waitKey(0)

# ---- 6. Histogram Equalization (Kontrast Normalizasyonu) ----
gray_uint8 = np.uint8(gray)
hist_eq = cv.equalizeHist(gray_uint8)
cv.imshow("Histogram Equalization", hist_eq)
cv.waitKey(0)

cv.destroyAllWindows()
