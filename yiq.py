import cv2
import numpy as np

def RGB_TO_YIQ(img):
    b = img[:, :, 0] 
    g = img[:, :, 1] 
    r = img[:, :, 2]

    yiq = np.empty_like(img)

    # Y
    yiq[:,:,0] = 0.299 * r + 0.587 * g + 0.114 * b
    # I
    yiq[:,:,1] = 0.596 * r - 0.275 * g - 0.321 * b
    # Q
    yiq[:,:,2] = 0.212 * r - 0.523 * g + 0.311 * b

    return np.uint8(yiq)