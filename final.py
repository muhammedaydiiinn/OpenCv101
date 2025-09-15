import cv2 as cv
import numpy as np

# Video kaynağı
capture = cv.VideoCapture(0)

# Video özelliklerini al
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
fps = capture.get(cv.CAP_PROP_FPS)

print(f"fps: {fps}, width: {width}, height: {height}")

# OpenCV'nin önceden eğitilmiş yüz tanıma modelini (Haar Cascade) yükle
# Bu dosya OpenCV kurulumu ile birlikte gelir, bu yol genellikle çalışır.
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')


def process(image, opt=1):
    """
    Görüntüyü seçilen seçeneğe göre işler.
    opt=0: Görüntünün tersini alır (bitwise_not).
    opt=1: Tüm görüntüyü bulanıklaştırır.
    opt=2: Kenarları tespit eder (Canny).
    opt=3: Arka Planı Bulanıklaştırır (Portre Modu).
    opt=4: Sadece Yüzü Bulanıklaştırır (Anonimleştirme).
    """
    if opt == 0:
        return cv.bitwise_not(image)

    if opt == 1:
        # (0,0) çekirdek boyutu, standart sapmadan (15) hesaplanmasını sağlar.
        return cv.GaussianBlur(image, (0, 0), 15)

    if opt == 2:
        return cv.Canny(image, 100, 200)

    # --- Yüz Tespiti ve Buna Bağlı İşlemler ---
    # Gri tonlama, yüz tespiti için daha hızlı ve verimlidir.
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # Yüzleri algıla. faces, bulunan her yüz için (x, y, w, h) bilgilerini içeren bir listedir.
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if opt == 3:  # Arka Planı Bulanıklaştır (Portre Modu)
        # 1. Orijinal görüntünün tamamını bulanıklaştır. Kernel boyutu (99,99) yüksek bulanıklık sağlar.
        blurred_image = cv.GaussianBlur(image, (99, 99), 0)

        # 2. Algılanan her yüz için işlem yap.
        for (x, y, w, h) in faces:
            # 3. Orijinal (net) görüntüden yüz bölgesini (ROI - Region of Interest) al.
            sharp_face = image[y:y + h, x:x + w]
            # 4. Bulanıklaştırılmış görüntünün aynı bölgesine, net yüzü yerleştir.
            blurred_image[y:y + h, x:x + w] = sharp_face

        return blurred_image

    if opt == 4:  # Sadece Yüzü Bulanıklaştır (Anonimleştirme)
        # Orijinal görüntü üzerinde değişiklik yapmak için bir kopyasını alalım.
        result_image = image.copy()

        # Algılanan her yüz için işlem yap.
        for (x, y, w, h) in faces:
            # 1. Orijinal görüntüden yüz bölgesini (ROI) al.
            face_roi = result_image[y:y + h, x:x + w]
            # 2. Sadece bu yüz bölgesini kuvvetli bir şekilde bulanıklaştır.
            blurred_face = cv.GaussianBlur(face_roi, (99, 99), 0)
            # 3. Orijinal görüntünün ilgili alanına bu bulanık yüzü geri yerleştir.
            result_image[y:y + h, x:x + w] = blurred_face

        return result_image

    # Eğer yüz bulunamazsa veya geçersiz bir seçenekse orijinal görüntüyü döndür
    return image


# Başlangıçta "Arka Planı Bulanıklaştır" efekti seçili olsun.
# '1'->0, '2'->1, '3'->2, '4'->3, '5'->4
index = 3

while True:
    ret, frame = capture.read()
    if ret:
        # Görüntüyü yatay olarak çevir (ayna efekti)
        frame = cv.flip(frame, 1)

        cv.imshow("Orjinal Goruntu", frame)

        # Seçilen indekse göre görüntüyü işle
        result = process(frame, index)
        cv.imshow("Islenmis Goruntu", result)

        c = cv.waitKey(50)

        # '1' ile '5' arasındaki tuşlara basıldığında index'i güncelle
        if c >= 49 and c <= 53:  # ASCII: '1'=49, '5'=53
            index = c - 49

        # ESC tuşuna basıldığında döngüden çık
        if c == 27:
            break
    else:
        break

capture.release()
cv.destroyAllWindows()