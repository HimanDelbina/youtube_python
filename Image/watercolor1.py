import cv2
import numpy as np


image = cv2.imread('1.png')
# new_image = cv2.resize(img, (1000,1200))
scale = float(2000)/(image.shape[0]+image.shape[1])
image = cv2.resize(
    image, (int(image.shape[1]*scale), int(image.shape[0]*scale)))

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
adjust_v = (img_hsv[:, :, 2].astype(np.uint8)+5)*3
adjust_v = ((adjust_v > 255)*255+(adjust_v <= 255)*adjust_v).astype(np.uint8)
img_hsv[:, :, 2] = adjust_v
img_soft = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
img_soft = cv2.GaussianBlur(img_soft, (51, 51), 0)

img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_grey = cv2.equalizeHist(img_grey)
invert = cv2.bitwise_not(img_grey)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(img_grey, invertedblur, scale=265.0)
sketch = cv2.merge([sketch, sketch, sketch])

img_water = ((sketch/255.0)*img_soft).astype(np.uint8)

cv2.imshow('img_water', img_water)
# cv2.imwrite("D:\Python36\siva_written.jpg",pencil_jc)
cv2.waitKey(0)
cv2.destroyAllWindows()