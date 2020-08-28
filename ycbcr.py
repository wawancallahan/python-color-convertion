import cv2
import numpy as np

def RGB_TO_YCBCR(img):
    b = img[:, :, 0] 
    g = img[:, :, 1] 
    r = img[:, :, 2]

    cbcr = np.empty_like(img)

    # Y
    cbcr[:,:,0] = .299 * r + .587 * g + .114 * b
    # Cr
    cbcr[:,:,1] = 128 + .5 * r - .419 * g - .081 * b
    # Cb
    cbcr[:,:,2] = 128 - .169 * r - .331 * g + .5 * b

    return np.uint8(cbcr)