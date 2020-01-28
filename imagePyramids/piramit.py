import cv2
import numpy as np

resim = cv2.imread("elma.jpg")
#resim Boyutu --- (225,225,3)
print(resim.shape)

cv2.imshow("Elma image",resim)
iki_kat = cv2.pyrUp(resim)
iki_kat_kucuk = cv2.pyrDown(resim)
cv2.imshow("iki kati",iki_kat)
cv2.imshow(
    "iki kat kücük",iki_kat_kucuk)
#iki kati alınmış Hali --- (450, 450, 3)
print(iki_kat.shape)

#iki kat kücük Hali
print((iki_kat_kucuk.shape))

cv2.waitKey(0)
cv2.destroyAllWindows()


