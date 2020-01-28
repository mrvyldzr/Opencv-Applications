import cv2
import numpy as np

resim = cv2.imread("OUTH.jpg")

print(resim[50,50])
resim[50,50] = [255,255,255]

print("Resim Ozelliği =" + str(resim.shape))
print("Resim Boyutu =" + str(resim.size))
print("Resim bit degeri" + str(resim.dtype))



#print(cv2.split(resim))
b,g,r = cv2.split(resim)

liste = [1,2,3]
bir,iki,uc = liste

cv2.imshow("OUTH orjinal resim" , resim)
cv2.imshow("OUTH Blue" , bir)
cv2.imshow("OUTH Green" , iki)
cv2.imshow("OUTH Red" , uc)


cv2.waitKey(0)
cv2.destroyAllWindows()