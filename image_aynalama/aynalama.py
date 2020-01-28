import cv2
import numpy as np
resim = cv2.imread("civciv.jpg")
#kare alma
print(resim[50,50])
cv2.rectangle(resim,(50,150),(150,20),[0,0,255],2)
cv2.rect

cv2.imshow("civciv",resim)

"""
#resim Uzatma
uzatilan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

#resmi aynalama
aynalanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#resmi Tekrar Etme
tekrar_edilen_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

#resmi Etrafını Sarma
etrafini_sarma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value= (255,0,0))

cv2.imshow("Civciv orjinal",resim)
cv2.imshow("Civciv uzatma", uzatilan_resim)
cv2.imshow("Civciv aynalama",aynalanan_resim)
cv2.imshow("Civciv tekrar etme ",tekrar_edilen_resim)
cv2.imshow("Civciv etrafini sarma",etrafini_sarma)
"""
cv2.waitKey(0)
cv2.destroyAllWindows()