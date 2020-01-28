import cv2
import numpy as np
resim = cv2.imread("hanslanda.jpg",0)

print(resim.item(100,100),0)
print(resim.item(100,100),1)
print(resim.item(100,100),2)

print(resim.shape)


cv2.imshow("hans landa",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()