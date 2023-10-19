import cv2
import matplotlib.pyplot as plt


img = cv2.imread('1.png')
new_image = cv2.resize(img, (1000, 1000))
# res = cv2.xphoto.oilPainting(new_image, 2, 1)
# res = cv2.stylization(new_image, sigma_s=60, sigma_r=0.6)
dst_gray, dst_color = cv2.pencilSketch(
    new_image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imshow('new_image', dst_gray)
# cv2.imwrite("D:\Python36\siva_written.jpg",pencil_jc)
cv2.waitKey(0)
cv2.destroyAllWindows()