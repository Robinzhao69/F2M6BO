import cv2
import time
import sys
import os


def een():
    print("typ a of w\n")
    img_path = 'images/product1.png'
    img = cv2.imread(img_path, -1)
    img = cv2.resize(img, (420, 69))
    
    cv2.imshow('Image', img)   
    cv2.waitKey(1)    

    key_pressed = cv2.waitKey(0) & 0xFF
    if key_pressed == ord('a'):
        cv2.destroyAllWindows()
        twee()
    
    if key_pressed == ord('w'):
        cv2.destroyAllWindows()
        drie()
    


def twee():
    os.system("cls")
    img = cv2.imread('images/product1.png', -1)
    img = cv2.resize(img, (69, 420))

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drie():
    os.system("cls")
    img = cv2.imread('images/max.jpg', -1)
    img = cv2.resize(img, (420, 420))

    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))

    cv2.imshow('Rotated by -90 degrees', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
een()