import cv2
import numpy as np
from skimage import color, io
import hsi
import hsv
import cmyk
import ycbcr
import yiq
import yuv
import lab
import xyz

img = cv2.imread('./assets/peko.png')

# Convert to RGB First
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('original image', img)

# Convert to HSI => ?
convert_image_hsi = hsi.RGB_TO_HSI(img)
# convert_image_hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow('hsi image', convert_image_hsi)

# Convert to HSV => ?
convert_image_hsv = hsv.RGB_TO_HSV(img)
# convert_image_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv image', convert_image_hsv)

# Convert to CMYK => True
convert_image_cmyk = cmyk.RGB_TO_CMYK(img)
cv2.imshow('cmyk image', convert_image_cmyk)

# Convert to YCbCr => True
convert_image_ycbcr = ycbcr.RGB_TO_YCBCR(img)
cv2.imshow('ycbcr image', convert_image_ycbcr)

# Convert to YIQ => ?
convert_image_yiq = yiq.RGB_TO_YIQ(img)
cv2.imshow('yiq image', convert_image_yiq)

# Convert to YUV => YCbCr
convert_image_yuv = yuv.RGB_TO_YUV(img)
cv2.imshow('yuv image', convert_image_yuv)

# Convert to LAB => True
convert_image_lab = lab.RGB_TO_LAB(img)
cv2.imshow('lab image', convert_image_lab)

# Convert to XYZ => True
convert_image_xyz = xyz.RGB_TO_XYZ(img)
cv2.imshow('xyz image', convert_image_xyz)

# Convert to Gray
convert_image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', convert_image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
