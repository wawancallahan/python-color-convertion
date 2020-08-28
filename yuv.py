import numpy as np
import skimage
import cv2

def RGB_TO_YUV(img):

    b = img[:, :, 0] 
    g = img[:, :, 1] 
    r = img[:, :, 2]

    yuv = np.empty_like(img)

    # Y
    yuv[:,:,0] = 0.29900 * r - 0.16874 * g + 0.50000 * b
    # U
    yuv[:,:,1] = 128.0 + 0.58700 * r - 0.33126 * g - 0.41869 * b
    # V
    yuv[:,:,2] = 128.0 + 0.11400 * r + 0.500003 * g - 0.08131 * b

    return np.uint8(yuv)

def RGB_TO_YUV2(img):
    # Conversion matrix from rgb to yuv, transpose matrix is used to convert from yuv to rgb
    yuv_from_rgb = np.array([[ 0.299     ,  0.587     ,  0.114      ],
                        [-0.14714119, -0.28886916,  0.43601035 ],
                        [ 0.61497538, -0.51496512, -0.10001026 ]])

    # Optional. The next two line can be ignored if the image is already in normalized numpy array.
    # convert image array to numpy array and normalize it from 0-255 to 0-1 range
    new_img = np.asanyarray(img)
    new_img = skimage.img_as_float(new_img)

    # do conversion
    return new_img.dot(yuv_from_rgb.T.copy())

def RGB_TO_YUV3(img):
    b = img[:, :, 0] 
    g = img[:, :, 1] 
    r = img[:, :, 2]

    yuv = np.empty_like(img)

    # Y
    yuv[:,:,0] = 0.29900 * r - 0.147108 * g + 0.614777 * b
    # U
    yuv[:,:,1] =0.5 + 0.58700 * r - 0.288804 * g - 0.514799 * b
    # V
    yuv[:,:,2] =0.5 + 0.11400 * r + 0.435912 * g - 0.099978 * b

    return np.uint8(yuv)