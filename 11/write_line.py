import numpy as np
import cv2 as cv

# Siyah bir arka plan (görsel) oluşturulur
image = np.zeros((512, 512, 3), np.uint8)

for i in range(100000):
    # Her döngüde ekranı temizle
    image[:, :, :] = 0

    # Rastgele koordinatlar oluştur
    x1 = np.random.rand() * 512
    y1 = np.random.rand() * 512
    x2 = np.random.rand() * 512
    y2 = np.random.rand() * 512

    # Rastgele renkler (BGR formatında) oluştur
    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)

    # Rastgele bir çizgi çiz (np.int -> int olarak düzeltildi)
    cv.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (b, g, r), 4, cv.LINE_8, 0)

    # Rastgele bir dikdörtgen çiz (np.int -> int olarak düzeltildi)
    cv.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (b, g, r), 1, cv.LINE_8, 0)

    # Görseli göster
    cv.imshow("image", image)

    # 20 milisaniye bekle ve bir tuşa basılıp basılmadığını kontrol et
    c = cv.waitKey(20)

    # Eğer basılan tuş ESC (ASCII değeri 27) ise döngüyü kır
    if c == 27:
        break  # ESC

# Pencereleri kapat
cv.destroyAllWindows()