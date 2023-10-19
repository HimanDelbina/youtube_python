import cv2
import matplotlib.pyplot as plt


img = cv2.imread('1.png')
new_image = cv2.resize(img, (1000,1000))
dst = cv2.edgePreservingFilter(new_image, flags=1, sigma_s=60, sigma_r=0.4)
edge = cv2.detailEnhance(dst, sigma_s=10, sigma_r=0.15)
dst_gray, dst_color = cv2.pencilSketch(new_image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
dst_color = cv2.stylization(new_image, sigma_s=60, sigma_r=0.07)

# cv2.imshow('new_image',new_image)
# cv2.imshow('dst',dst)
# cv2.imshow('edge',edge)
# cv2.imshow('dst_gray',dst_gray)
cv2.imshow('dst_color',dst_color)
cv2.waitKey(0)
cv2.destroyAllWindows()