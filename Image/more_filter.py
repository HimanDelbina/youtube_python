from PIL import Image, ImageFilter

#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
#Create image object
img = Image.open('1.png')
#Applying the blur filter
img1 = img.filter(CONTOUR)
# img1 = img.filter(DETAIL)
# img1 = img.filter(EDGE_ENHANCE)
# img1 = img.filter(EDGE_ENHANCE_MORE)
# img1 = img.filter(FIND_EDGES)
# img1 = img.filter(SHARPEN)
# img1 = img.filter(BLUR)
# img1 = img.filter(EMBOSS)
# img1 = img.filter(SMOOTH)
# img1 = img.filter(SMOOTH_MORE)
# img1.save('ImageFilter_blur.jpg')
img1.show()