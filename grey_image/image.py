import cv2
import  numpy as np
resim = cv2.imread("HIMYM.jpg",0)

cv2.imwrite("HIMYM_grey.jpg",resim)
cv2.imshow("HIMYM image",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

