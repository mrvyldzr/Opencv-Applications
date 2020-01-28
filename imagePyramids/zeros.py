import cv2
import numpy as np

def main():
    resim = np.zeros((400,400,3),dtype= "uint8") #400 e 400 lük matris oluşturuyor

    cv2.imshow("Resim", resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()