import cv2 as cv

# ---- 1. Görselin yolu ----
path = "data/"
img = cv.imread(path + "tech_pp.png")   # Görseli oku

# ---- 2. Görsel başarıyla okundu mu kontrol edelim ----
if img is None:
    print("Görsel okunamadı! Lütfen path'i kontrol et.")
    exit()

print("Görsel boyutu:", img.shape)  # (yükseklik, genişlik, kanal sayısı)

# ---- 3. Orijinal Görseli Göster ----
cv.namedWindow("Original Image", cv.WINDOW_AUTOSIZE)  # Pencere oluştur
cv.imshow("Original Image", img)                      # Görseli göster
cv.waitKey(0)  # Bir tuşa basılmasını bekle


# ---- 4. Renk Haritası (ColorMap) Uygula ----
# cv.COLORMAP_AUTUMN → Sarıdan kırmızıya geçiş (sonbahar rengi).
# cv.COLORMAP_BONE → Gri–mavi tonlar, X-ray etkisi.
# cv.COLORMAP_JET → Mavi → Yeşil → Kırmızı (ısı haritası için çok popüler).
# cv.COLORMAP_WINTER → Mavi → Yeşil geçişi.
# cv.COLORMAP_RAINBOW → Tam spektrum, gökkuşağı.
# cv.COLORMAP_OCEAN → Mavi–turuncu geçiş.
# cv.COLORMAP_HOT → Siyah → Kırmızı → Sarı → Beyaz.
# cv.COLORMAP_PINK → Pembe tonlar, bilimsel çizimler için.
# cv.COLORMAP_COOL → Cam göbeği → Pembe.


# Denemek istediğimiz colormap'ler
colormaps = [
    ("AUTUMN", cv.COLORMAP_AUTUMN),
    ("BONE", cv.COLORMAP_BONE),
    ("JET", cv.COLORMAP_JET),
    ("WINTER", cv.COLORMAP_WINTER),
    ("RAINBOW", cv.COLORMAP_RAINBOW),
    ("OCEAN", cv.COLORMAP_OCEAN),
    ("HOT", cv.COLORMAP_HOT),
    ("PINK", cv.COLORMAP_PINK),
    ("COOL", cv.COLORMAP_COOL),
]

for name, cmap in colormaps:
    dst = cv.applyColorMap(img, cmap)
    cv.imshow(name, dst)
    cv.waitKey(0)


# cvtColor
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(0)

cv.imwrite("data/gray.png", gray)

# ---- 6. Pencereleri Kapat ----
cv.destroyAllWindows()
